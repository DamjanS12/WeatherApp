import React, { useEffect, useRef, useState } from "react";
import './weather.css';
import search_icon from '../assets/search.png';
import clear_icon from '../assets/clear.png';
import cloud_icon from '../assets/cloud.png';
import drizzle_icon from '../assets/drizzle.png';
import humid_icon from '../assets/humidity.png';
import rain_icon from '../assets/rain.png';
import snow_icon from '../assets/snow.png';
import wind_icon from '../assets/wind.png';
import pollution_icon from '../assets/pollution.png'; 

const Weather = () => {
    const inputRef = useRef<HTMLInputElement>(null);
    const [weatherData, setWeatherData] = useState<any>(null);
    const [pollutionData, setPollutionData] = useState<any>(null); 

    const allicons: { [key: string]: string } = {
        "01d": clear_icon,
        "01n": clear_icon,
        "02d": cloud_icon,
        "02n": cloud_icon,
        "03d": cloud_icon,
        "03n": cloud_icon,
        "04d": drizzle_icon,
        "04n": drizzle_icon,
        "09d": rain_icon,
        "09n": rain_icon,
        "10d": rain_icon,
        "10n": rain_icon,
        "13d": snow_icon,
        "13n": snow_icon,
    };

    const search = async (city: string) => {
        if (city === "") {
            alert("Enter City Name!");
            return;
        }
        try {
            const url = `http://127.0.0.1:8000/weather_by_location?location=${city}`;
            const response = await fetch(url);
            const data = await response.json();

            const iconKey = data.weather[0]?.icon; 
            const icon = allicons[iconKey] || clear_icon;

            setWeatherData({
                humidity: data.main.humidity,
                windspeed: data.wind.speed,
                temperature: Math.floor(data.main.temp),
                location: data.name,
                icon: icon
            });

            const pollution = data.airpollution.list[0].components; 
            setPollutionData({
                pm25: pollution.pm2_5,
                pm10: pollution.pm10,
                aqi: data.airpollution.list[0].main.aqi
            });
        } catch (error) {
        alert("Location not found");
        console.error("Error:", error)

        }
    };

    useEffect(() => {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(async (position) => {
                const lat = position.coords.latitude;
                const lon = position.coords.longitude;
                try {
                    const url = `http://127.0.0.1:8000/weather_and_pollution_location?lat=${lat}&lon=${lon}`;
                    const response = await fetch(url);
                    const data = await response.json();
                    const weatherData = data.weather;

                    const iconKey = data.weather[0]?.icon; 
                    const icon = allicons[iconKey] || clear_icon;

                    setWeatherData({
                        humidity: weatherData.main.humidity,
                        windspeed: weatherData.wind.speed,
                        temperature: Math.floor(weatherData.main.temp),
                        location: weatherData.name,
                        icon: icon
                    });

           const pollution = data.airpollution.list[0].components;
                    setPollutionData({
                        pm25: pollution.pm2_5,
                        pm10: pollution.pm10,
                        aqi: data.airpollution.list[0].main.aqi
                    });

                } catch (error) {
                    console.error('Error fetching data', error);
                }
            });
        }
    }, []);

    return (
        <div className="weather">
            <div className="search-bar">
                <input ref={inputRef} type="text" placeholder="Search city" />
                <img src={search_icon} alt="search" onClick={() => search(inputRef.current?.value || "")} />
            </div>
            {weatherData && (
                <>
                    <img src={weatherData.icon} alt="weather icon" className="weather-icon" />
                    <p className="temperature">{weatherData.temperature}°C</p>
                    <p className="location">{weatherData.location}</p>
                    <div className="weather-data">
                        <div className="col">
                            <img src={humid_icon} alt="humidity" />
                            <div>
                                <p>{weatherData.humidity}%</p>
                                <span>Humidity</span>
                            </div>
                        </div>
                        <div className="col">
                            <img src={wind_icon} alt="wind" />
                            <div>
                                <p>{weatherData.windspeed} m/s</p>
                                <span>Wind Speed</span>
                            </div>
                        </div>
                        {pollutionData && (
                            <div className="col">
                                <img src={pollution_icon} alt="pollution" />
                                <div>
                                    <p>PM2.5: {pollutionData.pm25}</p>
                                    <p>PM10: {pollutionData.pm10}</p>
                                    <span>Air Quality Index (AQI): {pollutionData.aqi}</span>
                                </div>
                            </div>
                        )}
                    </div>
                </>
            )}
        </div>
    );
};

export default Weather;

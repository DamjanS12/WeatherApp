This WeatherApp leverages the OpenWeather API to provide weather and air pollution data. The application uses FastAPI for the backend to fetch data from the OpenWeather API and React for the frontend to display the information. When a user enters the page, the app automatically retrieves weather and pollution information based on the user's current geolocation. Additionally, users can search for weather information by entering a city name.


FEATURES:
-Geolocation-based Weather: Automatically displays the current weather and pollution data based on the user's location.
-Search by Location: Allows users to search for weather and pollution information for any city by entering the city name.

WEATHER INFORMATION:
-Temperature (in Celsius)
-Humidity (%)
-Wind Speed (m/s)
-Weather conditions (clear, cloudy, rain, etc.)

AIR POLLUTION INFORMATION:
-PM2.5 and PM10 levels
-Air Quality Index (AQI)

TECHNOLOGY STACK:
-Backend: FastAPI (Python)
-Frontend: React (JavaScript/TypeScript)
-API: OpenWeather API for fetching weather and pollution data
-Deployment: Docker 
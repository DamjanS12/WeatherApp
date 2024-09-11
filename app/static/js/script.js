document.getElementById('getWeather').addEventListener('click', () => {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(async (position) => {
            const lat = position.coords.latitude;
            const lon = position.coords.longitude;

            const response = await fetch(`/weather_and_pollution_location?lat=${lat}&lon=${lon}`);
            const data = await response.json();
            
            document.getElementById('result').innerText = JSON.stringify(data, null, 2);
        }, (error) => {
            console.error('Error getting location', error);
        });
    } else {
        console.error('Geolocation is not supported by this browser.');
    }
});
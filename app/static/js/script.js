<<<<<<< HEAD
window.onload = () => {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(getPostion); 

async function getPostion(position){

    const lat = position.coords.latitude;
    const lon = position.coords.longitude;

    const response = await fetch(`/weather_and_pollution_location?lat=${lat}&lon=${lon}`);
    const data = await response.json();
            
    document.getElementById('result').innerText = JSON.stringify(data, null, 2);
        };
    }
};
=======
document.getElementById('getWeather').addEventListener('click', () => {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(async (position) => {
            const lat = position.coords.latitude;
            const lon = position.coords.longitude;

            const response = await fetch(`/weather_and_pollution_location?lat=${lat}&lon=${lon}`);
            const data = await response.json();
            
            document.getElementById('result').innerText = JSON.stringify(data, null, 2);
        },) 
    } 
});
>>>>>>> 92961ec (Updated code and added frontend)

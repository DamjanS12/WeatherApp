import httpx
from typing import Any
from fastapi import APIRouter
from app.core.config import settings

router = APIRouter()

@router.get("/weather_and_pollution_location")
async def get_weather_and_pollution_current_location(lat: float, lon: float) -> Any:
    async with httpx.AsyncClient() as client:
        weather_data = await client.get(
            settings.CURRENT_WEATHER_LON_LAT_URL,
            params={"lat": lat, "lon": lon, "appid": settings.OPENWEATHERMAP_API_KEY, "units": "metric"}
        )
        pollution_data = await client.get(
            settings.AIR_POLLUTION_URL,
            params={"lat": lat, "lon": lon, "appid": settings.OPENWEATHERMAP_API_KEY}
        )
    weather_and_pollution_data = {
        "weather": weather_data.json(),
        "airpollution": pollution_data.json()
    }
    return weather_and_pollution_data

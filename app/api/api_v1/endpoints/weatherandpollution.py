import httpx
from typing import Any, Optional
from fastapi import APIRouter, HTTPException
from app.core.config import settings

router = APIRouter()



@router.get("/weather_and_pollution")
async def get_weather_and_pollution(lat: float, lon: float) -> Any:
    
    async with httpx.AsyncClient() as client:
       weather_data = await client.get(
             settings.CURRENT_WEATHER_URL,
            params={"lat": lat, "lon": lon, "appid": settings.OPENWEATHERMAP_API_KEY, "units": "metric"}
            )
       
       
    async with httpx.AsyncClient() as client:
        pollution_data = await client.get(
            settings.AIR_POLLUTION_URL,
            params={"lat": lat, "lon": lon, "appid": settings.OPENWEATHERMAP_API_KEY}
        )
    
    weather_and_pollution_data = {
        "weather": weather_data.json(),
        "airpollution": pollution_data.json()
    }
    
    return weather_and_pollution_data
    
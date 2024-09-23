import httpx
from typing import Any, Optional
from fastapi import APIRouter, HTTPException
from app.core.config import settings

router = APIRouter()

@router.get("/weather_and_pollution_location")
async def get_weather_and_pollution_current_location(lat: Optional[float], lon: Optional[float]) -> Any:
    
    async with httpx.AsyncClient() as client:
        weather_data = await client.get(
            settings.CURRENT_WEATHER_LON_LAT_URL,
            params={"lat": lat, "lon": lon, "appid": settings.OPENWEATHERMAP_API_KEY, "units": "metric"}
        )
        
        if weather_data.status_code != 200:
            raise HTTPException(status_code=weather_data.status_code, detail=weather_data.text)
        
        pollution_data = await client.get(
            settings.AIR_POLLUTION_URL,
            params={"lat": lat, "lon": lon, "appid": settings.OPENWEATHERMAP_API_KEY}
        )
        
        if pollution_data.status_code != 200:
            raise HTTPException(status_code=pollution_data.status_code, detail=pollution_data.text)
    
    weather_and_pollution_data = {
        "weather": weather_data.json(),
        "airpollution": pollution_data.json()
    }
    
    return weather_and_pollution_data


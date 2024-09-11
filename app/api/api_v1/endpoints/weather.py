import httpx
from typing import Any, Optional
from fastapi import APIRouter, HTTPException, Request
from app.core.config import settings

router = APIRouter()

@router.get("/weather_by_location")
async def get_current_weather(location: str) -> Any:
    
    async with httpx.AsyncClient() as client:
        data = await client.get(
            settings.CURRENT_WEATHER_URL,
            params={"q": location, "appid": settings.OPENWEATHERMAP_API_KEY, "units": "metric"}
        )

    
    return data.json()


@router.get("/weather")
async def get_current_weather_by_coords(lat: float, lon: float) -> Any:
    async with httpx.AsyncClient() as client:
        data = await client.get(
            settings.CURRENT_WEATHER_URL,
            params={"lat": lat, "lon": lon, "appid": settings.OPENWEATHERMAP_API_KEY, "units": "metric"}
        )
 

    return data.json()


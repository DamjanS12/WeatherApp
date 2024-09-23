from urllib import request
import httpx
from typing import Any
from fastapi import APIRouter
import json
import requests
from typing import Any, Optional
from fastapi import APIRouter, HTTPException, Request
from app.core.config import settings

router = APIRouter()

import httpx
from typing import Any
from fastapi import APIRouter, HTTPException
from app.core.config import settings

router = APIRouter()

@router.get("/weather_by_location")
async def get_current_weather(location: str) -> Any:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            settings.CURRENT_WEATHER_URL,
            params={"q": location, "appid": settings.OPENWEATHERMAP_API_KEY, "units": "metric"}
        )

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)

        coord_data = response.json()
        lat = coord_data["coord"]["lat"]
        lon = coord_data["coord"]["lon"]

        weather_response = await client.get(
            settings.CURRENT_WEATHER_URL,
            params={"lat": lat, "lon": lon, "appid": settings.OPENWEATHERMAP_API_KEY, "units": "metric"}
        )

        if weather_response.status_code != 200:
            raise HTTPException(status_code=weather_response.status_code, detail=weather_response.text)

        return weather_response.json()

@router.get("/weather")
async def get_current_weather_by_coords(lat: float, lon: float) -> Any:
        data = await request.get(
            settings.CURRENT_WEATHER_LON_LAT_URL,
            params={"lat": lat, "lon": lon, "appid": settings.OPENWEATHERMAP_API_KEY, "units": "metric"}
        )
        
        if data.status_code != 200:
            raise HTTPException(status_code=data.status_code, detail=data.text)
        return data.json()

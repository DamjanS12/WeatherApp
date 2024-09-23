import httpx
from typing import Any, Optional
from fastapi import APIRouter, HTTPException
from app.core.config import settings

router = APIRouter()


@router.get("/air-pollution")
async def get_air_pollution(lat: float,lon: float) -> Any:
    
    async with httpx.AsyncClient() as client:
        data = await client.get(
            settings.AIR_POLLUTION_URL,
            params={"lat": lat, "lon": lon, "appid": settings.OPENWEATHERMAP_API_KEY}
            )
        
        if data.status_code != 200:
            raise HTTPException(status_code=data.status_code, detail=data.text)

    return data.json()
    



from fastapi import APIRouter
from app.api.api_v1.endpoints import air_pollution, weather, weatherandpollution

api_router = APIRouter()
api_router.include_router(weather.router)
api_router.include_router(air_pollution.router)
api_router.include_router(weatherandpollution.router)

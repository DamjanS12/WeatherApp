import secrets
from typing import List, Optional, Union
from pydantic_settings import BaseSettings 


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Project WeatherApp"
    OPENWEATHERMAP_API_KEY: str
    CURRENT_WEATHER_URL: str
    CURRENT_WEATHER_LON_LAT_URL: str
    AIR_POLLUTION_URL: str
    SERVER_NAME: str   
    SERVER_HOST: str   
    BACKEND_CORS_ORIGINS: list[str]

    class Config:
        case_sensitive = True
        env_file_encoding = "utf-8"
        __test__ = False  
        env_file = ".env"


settings = Settings()

print("ENVIRONMENT: ")
print(settings)

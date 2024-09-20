import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.api.api_v1.api import api_router
from app.core.config import settings
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse


app = FastAPI(title=settings.PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/")
async def serve_index():
    return FileResponse("app/static/index.html")


app.mount("/static", StaticFiles(directory="app/static/react-app"), name="static")


@app.get("/")
async def serve_index():
    return FileResponse("app/static/react-app/index.html")


app.include_router(api_router)

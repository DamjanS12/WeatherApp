import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.api_v1.api import api_router  # Adjust the import based on your structure
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="app/static/react-app"), name="static")

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI backend!"}

app.include_router(api_router)  

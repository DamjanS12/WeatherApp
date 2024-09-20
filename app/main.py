from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.api.api_v1.api import api_router
from app.core.config import settings

# Create the FastAPI app
app = FastAPI(title=settings.PROJECT_NAME)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174"],  # Allow your React app
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="app/static/react-app"), name="static")

# Define the route for serving the index
@app.get("/")
async def serve_index():
    return FileResponse("app/static/react-app/index.html")

# Include your API router
app.include_router(api_router)

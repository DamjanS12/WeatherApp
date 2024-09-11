from fastapi import FastAPI
from app.api.api_v1.api import api_router
from app.core.config import settings
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse



app = FastAPI(
    title=settings.PROJECT_NAME
)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
async def serve_index():
    return FileResponse("app/static/index.html")


app.include_router(api_router)

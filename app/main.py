from fastapi import FastAPI

from app.routes.health import router as health_router

app = FastAPI(
    title="api-importacion",
    description="API de importación",
    version="0.1.0",
)

app.include_router(health_router)

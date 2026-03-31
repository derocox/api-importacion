from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime, timezone

router = APIRouter(prefix="/health", tags=["health"])


class HealthResponse(BaseModel):
    status: str
    timestamp: str
    version: str


@router.get("", response_model=HealthResponse, summary="Health check")
def health_check() -> HealthResponse:
    """Verifica que la API está activa y responde correctamente."""
    return HealthResponse(
        status="ok",
        timestamp=datetime.now(timezone.utc).isoformat(),
        version="0.1.0",
    )

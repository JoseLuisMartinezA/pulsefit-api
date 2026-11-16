"""Endpoint de verificación de estado y salud del servicio."""
from fastapi import APIRouter
from datetime import datetime, timezone
from app.core.config import settings

router = APIRouter()

START_TIME = datetime.now(timezone.utc)


@router.get(
    "/health",
    summary="Verificar salud de la API",
    description="Retorna el estado operativo actual, versión, tiempo de actividad y entorno de ejecución."
)
async def check_health():
    uptime_seconds = (datetime.now(timezone.utc) - START_TIME).total_seconds()
    return {
        "status": "healthy",
        "app_name": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "environment": "development",
        "uptime_seconds": round(uptime_seconds, 2),
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

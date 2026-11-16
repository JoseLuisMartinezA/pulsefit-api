"""Configuración global de la aplicación PulseFit."""
from pydantic import BaseModel
from typing import List


class Settings(BaseModel):
    PROJECT_NAME: str = "PulseFit API"
    VERSION: str = "0.1.0"
    DESCRIPTION: str = (
        "API RESTful para la gestión y monitorización del rendimiento deportivo, "
        "rutinas de entrenamiento y nutrición deportiva. Desarrollada para el módulo "
        "Programación de Aplicaciones Utilizando Frameworks (PDAU - 2º DAM)."
    )
    API_V1_STR: str = "/api/v1"
    
    # Configuración de CORS para admitir clientes web y móviles (UT2)
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost",
        "http://localhost:3000",
        "http://localhost:5173",
        "http://localhost:8080",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
    ]


settings = Settings()

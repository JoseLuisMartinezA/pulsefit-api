"""Punto de entrada de la aplicación FastAPI PulseFit API.
Módulo: Programación de Aplicaciones Utilizando Frameworks (PDAU - 2º DAM).
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1.api_router import api_router

# Inicialización de la aplicación FastAPI con metadatos OpenAPI
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configuración del middleware de CORS para admitir peticiones desde clientes (UT2)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar enrutador de la API versión 1
app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/", tags=["Información General"])
async def root():
    """Endpoint raíz que retorna información del proyecto y accesos directos."""
    return {
        "message": f"¡Bienvenido a {settings.PROJECT_NAME}!",
        "version": settings.VERSION,
        "author": "José - 2º DAMEL",
        "module": "Programación de Aplicaciones Utilizando Frameworks (PDAU)",
        "docs_url": "/docs",
        "redoc_url": "/redoc",
        "api_v1": settings.API_V1_STR
    }

"""Enrutador principal de la API versión 1."""
from fastapi import APIRouter
from app.api.v1.endpoints import health, exercises

api_router = APIRouter()

api_router.include_router(health.router, tags=["Salud del Sistema"])
api_router.include_router(exercises.router, prefix="/exercises", tags=["Catálogo de Ejercicios"])

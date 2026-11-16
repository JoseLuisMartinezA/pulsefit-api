"""Esquemas de validación y transferencia de datos (DTO) para Ejercicios."""
from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class MuscleGroup(str, Enum):
    CHEST = "Pectoral"
    BACK = "Espalda"
    LEGS = "Piernas"
    SHOULDERS = "Hombros"
    ARMS = "Brazos"
    CORE = "Abdomen / Core"


class ExerciseBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, description="Nombre descriptivo del ejercicio")
    muscle_group: MuscleGroup = Field(..., description="Grupo muscular principal trabajado")
    equipment: str = Field(default="Peso corporal", description="Material o máquina requerida")
    description: Optional[str] = Field(None, description="Instrucciones técnicas de ejecución")


class ExerciseCreate(ExerciseBase):
    pass


class ExerciseResponse(ExerciseBase):
    id: int = Field(..., description="Identificador único del ejercicio")
    is_active: bool = Field(default=True, description="Indica si el ejercicio está disponible en el catálogo")

    class Config:
        from_attributes = True

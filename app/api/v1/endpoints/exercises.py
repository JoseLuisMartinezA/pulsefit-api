"""Endpoints REST para la gestión del catálogo de ejercicios."""
from fastapi import APIRouter, HTTPException, status, Query
from typing import List, Optional
from app.schemas.exercise import ExerciseCreate, ExerciseResponse, MuscleGroup

router = APIRouter()

# Simulación de repositorio en memoria para el prototipo inicial de la UT1.2
# En la UT1.3 se conectará con SQLite/PostgreSQL mediante SQLAlchemy 2.0
DB_EXERCISES: List[dict] = [
    {
        "id": 1,
        "name": "Press de banca con barra",
        "muscle_group": MuscleGroup.CHEST,
        "equipment": "Barra olímpica y banco plano",
        "description": "Ejercicio compuesto para el desarrollo de fuerza y masa en pectoral, tríceps y deltoides.",
        "is_active": True
    },
    {
        "id": 2,
        "name": "Sentadilla trasera (Back Squat)",
        "muscle_group": MuscleGroup.LEGS,
        "equipment": "Barra y rack de sentadillas",
        "description": "Patrón de movimiento de flexión de rodilla dominante para cuádriceps, glúteos e isquios.",
        "is_active": True
    },
    {
        "id": 3,
        "name": "Dominadas pronas (Pull-ups)",
        "muscle_group": MuscleGroup.BACK,
        "equipment": "Barra de dominadas",
        "description": "Tracción vertical con peso corporal para dorsal ancho, redondo mayor y bíceps.",
        "is_active": True
    },
    {
        "id": 4,
        "name": "Press militar de pie con barra",
        "muscle_group": MuscleGroup.SHOULDERS,
        "equipment": "Barra olímpica",
        "description": "Empuje vertical estricto para el desarrollo de la cabeza anterior y lateral del deltoides.",
        "is_active": True
    }
]


@router.get(
    "/",
    response_model=List[ExerciseResponse],
    summary="Listar catálogo de ejercicios",
    description="Recupera la lista de ejercicios disponibles con soporte para filtrado por grupo muscular."
)
async def list_exercises(
    muscle_group: Optional[MuscleGroup] = Query(None, description="Filtrar por grupo muscular específico")
):
    if muscle_group:
        return [ex for ex in DB_EXERCISES if ex["muscle_group"] == muscle_group]
    return DB_EXERCISES


@router.get(
    "/{exercise_id}",
    response_model=ExerciseResponse,
    summary="Obtener un ejercicio por ID",
    description="Retorna los detalles técnicos de un ejercicio en base a su identificador numérico."
)
async def get_exercise(exercise_id: int):
    for ex in DB_EXERCISES:
        if ex["id"] == exercise_id:
            return ex
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Ejercicio con identificador {exercise_id} no encontrado en la base de datos."
    )


@router.post(
    "/",
    response_model=ExerciseResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crear nuevo ejercicio",
    description="Registra un nuevo ejercicio en el catálogo validando la estructura del cuerpo mediante Pydantic."
)
async def create_exercise(exercise_in: ExerciseCreate):
    new_id = len(DB_EXERCISES) + 1
    new_exercise = {
        "id": new_id,
        "name": exercise_in.name,
        "muscle_group": exercise_in.muscle_group,
        "equipment": exercise_in.equipment,
        "description": exercise_in.description,
        "is_active": True
    }
    DB_EXERCISES.append(new_exercise)
    return new_exercise

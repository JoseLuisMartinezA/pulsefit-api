"""Batería de pruebas automatizadas del proyecto PulseFit API."""
import unittest
import sys
import os

# Asegurar que el directorio raíz del proyecto está en el PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestPulseFitAPI(unittest.TestCase):
    def test_read_root(self):
        """Verifica que el endpoint raíz responda con código 200 y mensaje de bienvenida."""
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("message", data)
        self.assertEqual(data["version"], "0.1.0")
        self.assertEqual(data["docs_url"], "/docs")

    def test_health_check(self):
        """Verifica que el endpoint de salud responda con status healthy."""
        response = client.get("/api/v1/health")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "healthy")
        self.assertIn("uptime_seconds", data)

    def test_list_exercises(self):
        """Verifica la recuperación de la lista de ejercicios."""
        response = client.get("/api/v1/exercises/")
        self.assertEqual(response.status_code, 200)
        exercises = response.json()
        self.assertIsInstance(exercises, list)
        self.assertGreaterEqual(len(exercises), 1)

    def test_filter_exercises_by_muscle_group(self):
        """Verifica el filtrado por query parameter muscle_group."""
        response = client.get("/api/v1/exercises/?muscle_group=Espalda")
        self.assertEqual(response.status_code, 200)
        exercises = response.json()
        for ex in exercises:
            self.assertEqual(ex["muscle_group"], "Espalda")

    def test_get_exercise_by_id(self):
        """Verifica la obtención de un ejercicio existente."""
        response = client.get("/api/v1/exercises/1")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["name"], "Press de banca con barra")

    def test_get_exercise_not_found(self):
        """Verifica que un ID inexistente retorne código 404."""
        response = client.get("/api/v1/exercises/999")
        self.assertEqual(response.status_code, 404)

    def test_create_exercise(self):
        """Verifica la creación y validación de un nuevo ejercicio."""
        new_exercise = {
            "name": "Peso muerto rumano",
            "muscle_group": "Piernas",
            "equipment": "Barra y discos olímpicos",
            "description": "Trabajo de cadena posterior e isquiosurales."
        }
        response = client.post("/api/v1/exercises/", json=new_exercise)
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertEqual(data["name"], new_exercise["name"])
        self.assertEqual(data["muscle_group"], new_exercise["muscle_group"])
        self.assertIn("id", data)


if __name__ == "__main__":
    unittest.main()

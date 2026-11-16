# PulseFit API 🏋️‍♂️

> Backend RESTful desarrollado con **FastAPI** para la gestión integral de entrenamientos, rutinas deportivas y nutrición.
> Proyecto práctico del módulo **Programación de Aplicaciones Utilizando Frameworks (PDAU - 2º DAMEL)**.

---

## 📋 Descripción del Proyecto
**PulseFit API** es una solución backend de alto rendimiento diseñada con arquitectura modular en capas bajo el paradigma cliente-servidor desacoplado. En esta fase inicial (**Tarea UT1.2**), se implementa la base del proyecto, configuración del entorno, middlewares y los primeros endpoints RESTful con documentación automática interactiva en Swagger UI.

---

## 🛠️ Requisitos Previos
* **Python**: 3.11+ (Recomendado 3.11 o superior).
* **Git**: Control de versiones.

---

## 🚀 Puesta en Marcha en Local

### 1. Clonar el repositorio y acceder a la carpeta
```bash
git clone https://github.com/joseluis-dam/pulsefit-api.git
cd pulsefit-api
```

### 2. Crear y activar el entorno virtual
En Windows PowerShell:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

*(Nota: Si PowerShell restringe la ejecución de scripts, ejecutar previamente: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`)*.

En Linux/macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Ejecutar el servidor de desarrollo Uvicorn
```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

---

## 🌐 Endpoints y Verificación del Servidor

Una vez arrancado el servidor, se puede acceder a las siguientes URLs en el navegador o mediante herramientas como Postman / cURL:

| Ruta | Método | Descripción |
| :--- | :--- | :--- |
| `http://localhost:8000/` | `GET` | Información del proyecto y enlaces a la documentación |
| `http://localhost:8000/api/v1/health` | `GET` | Comprobación de estado del servicio y uptime |
| `http://localhost:8000/api/v1/exercises/` | `GET` | Listado del catálogo de ejercicios (soporta `?muscle_group=...`) |
| `http://localhost:8000/api/v1/exercises/{id}`| `GET` | Consulta detallada de ejercicio por ID |
| `http://localhost:8000/api/v1/exercises/` | `POST` | Creación de nuevo ejercicio con validación Pydantic |
| **`http://localhost:8000/docs`** | `GET` | **Documentación interactiva Swagger UI** |
| **`http://localhost:8000/redoc`** | `GET` | Documentación técnica alternativa ReDoc |

---

## 🧪 Ejecución de Pruebas Automatizadas
Para ejecutar la batería de pruebas unitarias:
```bash
python -m unittest discover -s tests
```

---

## 📂 Estructura del Proyecto
```
pulsefit-api/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── endpoints/
│   │       │   ├── exercises.py   # Controlador REST de ejercicios
│   │       │   └── health.py      # Controlador de healthcheck
│   │       └── api_router.py      # Enrutador centralizado v1
│   ├── core/
│   │   └── config.py              # Configuración y settings Pydantic
│   ├── schemas/
│   │   └── exercise.py            # Modelos DTO y validación Pydantic
│   ├── __init__.py
│   └── main.py                    # Aplicación FastAPI y middlewares (CORS)
├── tests/
│   ├── __init__.py
│   └── test_main.py               # Batería de tests con TestClient
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 👨‍💻 Autor
* **Alumno:** José (2º DAMEL)
* **Profesor:** Rubén Élez López
* **Módulo:** Programación de Aplicaciones Utilizando Frameworks (PDAU)

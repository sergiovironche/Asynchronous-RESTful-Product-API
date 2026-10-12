# Asynchronous RESTful Product API

API RESTful asíncrona para la gestión de un catálogo de productos e inventario, desarrollada con **FastAPI**, **SQLAlchemy 2.0** y **SQLite (`aiosqlite`)**, siguiendo una **Arquitectura en Capas (Clean Architecture)**.

---

## 🏗️ Arquitectura del Proyecto

El proyecto mantiene una estricta separación de responsabilidades organizada de la siguiente manera:

```text
project-root/
├── app/
│   ├── api/          # Capa de Controladores / Routers
│   ├── core/         # Configuración y Conexión Asíncrona a BD
│   ├── models/       # Modelos ORM (SQLAlchemy 2.0)
│   ├── schemas/      # DTOs y Validación de Datos (Pydantic V2)
│   ├── repositories/ # Capa de Acceso a Datos (AsyncSession)
│   └── services/     # Capa de Lógica de Negocio y Reglas
├── main.py           # Punto de Entrada de la Aplicación
├── requirements.txt  # Dependencias del Proyecto
├── tests.ps1         # Test Suite en PowerShell (cURL)
└── README.md
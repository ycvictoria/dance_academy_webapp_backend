
```markdown
# ⚙️ DanceAcademyApp - Backend API 🛡️

Esta es la API REST robusta y escalable que motoriza el ecosistema de **DanceAcademyApp**. Provee autenticación segura, control de acceso basado en roles (RBAC), procesamiento transaccional de compras de coreografías y agregaciones SQL optimizadas para reportes estadísticos comerciales.

---

## 🛠️ Stack Tecnológico

* **Lenguaje:** Python 3.11+ 🐍
* **Framework Principal:** Django 5.0 + Django REST Framework (DRF)
* **Base de Datos Relacional:** PostgreSQL (Supabase / Local)
* **Autenticación:** JWT (JSON Web Tokens) vía `djangorestframework-simplejwt`
* **Pruebas:** Django Test Cases (Unidades e Integración)

---

## 📦 Estructura del Proyecto

```text
backend/
├── core/                # Configuración global del proyecto Django (settings, urls)
├── apps/                # Aplicaciones modulares del negocio
│   ├── autenticacion/   # Lógica de Login, Registro, JWT y Roles (Admin, Profesor, Cliente)
│   ├── usuarios/        # CRUD de administración de usuarios internos
│   ├── coreografias/    # Catálogo de canciones, videos, reviews y streaming seguro
│   └── ventas/          # Modelado de Facturación, Ventas, Detalle y pasarela simulada
├── gestion_academia/    # Directorio raíz del entorno
├── manage.py            # CLI de comandos de Django
├── requirements.txt     # Dependencias empaquetadas del proyecto
└── .env.example         # Plantilla de secretos e hilos de conexión a la BD
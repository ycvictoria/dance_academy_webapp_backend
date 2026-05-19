
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

##⚙️ Configuración e Instalación Local
Sigue estos pasos detallados para configurar el entorno y levantar el servidor de desarrollo en tu máquina:

1. Navegar al directorio del Backend
Abre tu terminal y dirígete a la carpeta interna del backend:

Bash
cd backend
2. Crear y activar el entorno virtual (venv)
Aísla las dependencias del proyecto ejecutando el comando correspondiente a tu sistema operativo:

En Windows (Símbolo del sistema / PowerShell):

Bash
python -m venv venv
.\venv\Scripts\activate
En macOS / Linux:

Bash
python3 -m venv venv
source venv/bin/activate
3. Instalar las dependencias del proyecto
Asegúrate de tener pip actualizado e instala las librerías necesarias especificadas en el archivo de requerimientos:

Bash
pip install --upgrade pip
pip install -r requirements.txt
4. Configurar las Variables de Entorno
Crea un archivo llamado .env en la raíz de la carpeta backend/ basándote en la plantilla .env.example. Configura allí tus credenciales locales o de tu base de datos en la nube (ej. Supabase):

Fragmento de código
DEBUG=True
SECRET_KEY=tu_clave_secreta_django_personalizada
DB_NAME=postgres
DB_USER=tu_usuario_postgres
DB_PASSWORD=tu_contraseña_segura
DB_HOST=tu_host_de_supabase_o_localhost
DB_PORT=5432
5. Ejecutar Migraciones de Base de Datos
Prepara y despliega el esquema relacional en tu base de datos PostgreSQL:

Bash
python manage.py makemigrations
python manage.py migrate
6. Iniciar el Servidor de Desarrollo
Pon en marcha el backend local corriendo el script de ejecución de Django:

Bash
python manage.py runserver
La API se inicializará correctamente y estará escuchando peticiones en: http://127.0.0.1:8000/api/

🧪 Ejecución de Pruebas Automatizadas (Testing)
Para comprobar la integridad de la base de datos, la seguridad en las rutas protegidas, la autenticación por roles y el correcto funcionamiento de los endpoints, ejecuta la suite de pruebas:

Bash
python manage.py test
👥 Contribuidores del Backend
Desarrolladores Back-end:
CAMILO ANDRES RISCANEVO COTRINA
BRAYAN FERNANDO CRUZ PUERTA
FREDDY ALEXANDER MELO BUITRAGO 
VICTORIA YUAN CHEN
YISEIRI YANUA SATIZABAL ORTIZ

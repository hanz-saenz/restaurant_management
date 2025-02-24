
# Django Project

Este proyecto es una aplicación web creada con Django que incluye manejo de tareas asíncronas con Celery y Redis.

## Requisitos

- Python 3.8 o superior
- Docker
- Redis
- Celery
- PostgreSQL

## Clonar el Proyecto

Primero, clona el repositorio desde GitHub:

```bash
[git clone https://github.com/tu_usuario/tu_proyecto.git](https://github.com/hanz-saenz/restaurant_management.git)
cd tu_proyecto
```

## Crear y Activar el Entorno Virtual

Crea y activa un entorno virtual para aislar las dependencias del proyecto:

```bash
# Crear el entorno virtual
python -m venv env

# Activar el entorno en Windows
..\env\Scripts\activate

# Activar el entorno en macOS/Linux
source env/bin/activate
```

## Instalar Requisitos

Con el entorno virtual activado, instala los requisitos del proyecto:

```bash
pip install -r requirements.txt
```

## Descargar e Iniciar Redis con Docker

El proyecto requiere Redis como broker de mensajes para Celery. Puedes iniciar Redis utilizando Docker:

```bash
# Descargar la imagen de Redis
docker pull redis

# Iniciar un contenedor de Redis
docker run -d -p 6379:6379 --name redis-container redis
```

## Configurar el Proyecto

Antes de iniciar el proyecto, asegúrate de que las configuraciones de Redis y Celery estén correctas en tus archivos de configuración (generalmente en `settings.py` o en un archivo de configuración dedicado a Celery).

## Conectar a la Base de Datos PostgreSQL

Para conectarte a una base de datos PostgreSQL local, asegúrate de tener PostgreSQL instalado. Puedes conectarte utilizando el siguiente comando:

```bash
# Conectar a PostgreSQL
psql -U tu_usuario -d restaurant_management
```

Reemplaza `tu_usuario` con el nombre de tu usuario de PostgreSQL y `restaurant_management` con el nombre de la base de datos que estás utilizando.

### Restaurar una Copia de Seguridad (.backup)

Si tienes una copia de seguridad en formato `.backup`, puedes restaurarla con el siguiente comando:

```bash
# Restaurar una copia de seguridad .backup
pg_restore -U tu_usuario -d restaurant_management -1 restaurant_management.backup
```

Este comando restaurará el archivo `.backup` a la base de datos especificada.

## Migraciones de Base de Datos

Realiza las migraciones necesarias para la base de datos:

```bash
python manage.py migrate
```

## Iniciar el Proyecto de Django

Inicia el servidor de desarrollo de Django con el siguiente comando:

```bash
python manage.py runserver
```

El proyecto ahora debería estar disponible en [http://localhost:8000](http://localhost:8000).

## Iniciar Celery

Para iniciar Celery, usa el siguiente comando. Si estás en Windows, asegúrate de usar el argumento `--pool=threads`:

```bash
# En macOS/Linux
celery -A tu_proyecto worker --loglevel=info

# En Windows
celery -A tu_proyecto worker --loglevel=info --pool=threads
```

## Endpoints de la API

A continuación se listan las direcciones de las APIs disponibles en el proyecto:

### Restaurantes

- **Listar Restaurantes:** `GET /api/restaurants/`

- **Crear Restaurante:** ` POST /api/restaurants/create/`

- **Detalles de un Restaurante:** ` GET /api/restaurants/<int:pk>/`

- **Actualizar Restaurante:** ` PUT /api/restaurants/update/<int:pk>/`

- **Eliminar Restaurante:** ` DELETE /api/restaurants/delete/<int:pk>/`

### Usuarios

- **Listar Usuarios:** ` GET /api/users/`

- **Crear Usuario:** ` POST /api/users/create/`

- **Detalles de un Usuario:** ` GET /api/users/<int:pk>/`

- **Actualizar Usuario:** ` PUT /api/users/update/<int:pk>/`

- **Eliminar Usuario:** ` DELETE /api/users/delete/<int:pk>/`

### Órdenes

- **Listar Órdenes:** ` GET /api/orders/`

- **Crear Orden:** ` POST /api/orders/create/`

- **Detalles de una Orden:** ` GET /api/orders/<int:pk>/`

- **Actualizar Orden:** ` PUT /api/orders/update/<int:pk>/`

- **Eliminar Orden:** ` DELETE /api/orders/delete/<int:pk>/`

### Reportes

- **Generar Reporte de Ventas:** ` POST /api/restaurants/<int:restaurant_id>/generate-sales-report/`

- **Descargar Reporte:** ` GET /api/reports/download/<str:filename>/`

Consulta la documentación de cada API para más detalles sobre los endpoints y cómo utilizarlos.

---

¡Y eso es todo! Ya tienes tu entorno configurado, Redis corriendo, PostgreSQL conectado, y el proyecto de Django listo para usar.

## BASE DE PROYECTO

1. crear el entorno virtual  `python -m venv .venv`
2. Activar el entorno virtual
3. Instalar django `pip install django`
4. Inicializar el proyecto `django-admin startproject django_project .`
5. Se pone esto, en el settings de la carpeta creada `'DIRS': [BASE_DIR / 'templates'],`
6. Se puso el comando en la consola para crear una carpeta `django-admin startapp django_app`
## para agregar un nuevo usuario:
    ```bash
    python manage.py createsuperuser

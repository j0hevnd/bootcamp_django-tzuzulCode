# Proyecto Product Storage
### Proyecto realizado con Vistas basadas en clases

Proyecto creado con el fin de descubrir el potencial que nos da Django con sus Class-base View.

Usamos las vistas:
- View
- TemplateView
- CreateView
- DetailView
- UpdateView
- DeleteView
- FormView
- LoginView
- LogoutView

Uso de formularios dentro de Django y cómo los validamos.
Manejo de inicio de sesión y registro de usuarios

Subida de arhivos desde el HTML.

Modificación del panel de administración para manejar la forma como vemos nuestros modelos.


*El proyecto usa la base de datos POSTGRESQL.*

------
### Instalar dependencias y e iniciar el proyecto (Windows)

```
    # Crear un entorno virtual de python
    >>> python -m venv <nombre_entorno>

    # Activar el entorno (estar a la altura de la carpeta creada)
    >>> .\<nombre_entorno>\Scripts\activate (Windows)

    # A la altura del archivo requirements.txt del proyecto
    >>> pip install -r requirements.txt

    # A la altura del archivo manage.py, iniciamos el servidor
    >>> python manage.py runserver  (Esto para validar que funcione correctamente)

    # Iniciar las migraciones a la base de datos
    >>> python manage.py makemigrations
    >>> python manage.py migrate

    # Crear superusuario
    >>> python manage.py createsuperuser

    # Iniciar el servidor e 
    # ingresar al panel de administración del proyecto. Ingresar datos allí.
    http://127.0.0.1:8000/admin/ (validar que el puerto de salida sea el 8000)

```
# Proyecto blog
### Primer proyecto del bootcamp

Tendremos un blog funcional donde podremos agregar artículos nuevos al blog, listarlos por sus correspondientes categorías, ver cada uno por separado y una caja de comentarios al final de cada artículo.

Manejo de usuarios para registro e inicio de sesión. Los usuarios autenticados podrán comentar los artículos

**Frontend diseñado con la librería TailwindCss.**
*El proyecto usa la base de datos por defecto de Django, db.sqlite3.*

------
### Instalar dependencias y e iniciar el proyecto (Windows)

```
    # A la altura del archivo requirements.txt
    >>> pip install -r requirements.txt

    # A la altura del archivo manage.py
    >>> python manage.py runserver  (Esto para validar que funcione correctamente)

    # Iniciar las migraciones a la base de datos
    >>> python manage.py makemigrations
    >>> python manage.py migrate

    # Crear superusuario
    >>> python manage.py createsuperuser

    ## Ingresar al panel de administración del proyecto, e ingresar datos.
    http://127.0.0.1:8000/admin/ (validar que el puerto de salida sea el 8000)

```
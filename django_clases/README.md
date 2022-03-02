# Proyecto Product Storage
### Proyecto realizado con Vistas basadas en clases

Proyecto creado con el fin de descubrir el potencial que nos da Django con sus Class-base View
Usamos las vistas:
- View
- TemplateView
- CreateView
- DetailView
- UpdateView
- DeleteView
- FormView

Uso de formularios dentro de Django y como los validamos.

Subida de arhivos desde el HTML.

Modificación del panel de administración para manejar la forma como vemos nuestros modelos.


*El proyecto usa la base de datos POSTGRESQL.*

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
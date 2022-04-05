# Proyecto Movies
#### Proyecto introductorio a Django Rest Framework

### Conceptos usados:
- Vistas basadas en funciones 
- Vistas basadas en clases
- Serializers
- Viewsets
- Routers

*Validación dentro de los serializers.py*
*Métodos HTTP*
*Autententicacion y manejo de rest_framework.authtoken*
*Envío de emails*


------
### Instalar dependencias y e iniciar el proyecto (Windows)

```
    # Crear un entorno virtual de python
    >>> python -m venv <nombre_entorno>

    # Activar el entorno (estar a la altura de la carpeta creada)
    >>> .\<nombre_entorno>\Scripts\activate (Windows)

    # A la altura del archivo requirements.txt del proyecto
    >>> pip install -r requirements.txt

    # Iniciar las migraciones a la base de datos
    >>> python manage.py makemigrations
    >>> python manage.py migrate

    # Crear superusuario
    >>> python manage.py createsuperuser

    # A la altura del archivo manage.py, iniciamos el servidor
    >>> python manage.py runserver
```

### Rutas de aplicación

## Movies
- (POST) crear: http://127.0.0.1:8000/api/create-movies/
```
    {
        "movie_name": "Raplh",
        "description": "The destructor"
    }
```
- (GET) listar: http://127.0.0.1:8000/api/list-movies/
- (GET) detalle: http://127.0.0.1:8000/api/detail-movie/1/
- (PUT) actualizar: http://127.0.0.1:8000/api/update-movie/1/
```
    {
        "movie_name": "Raplh",
        "description": "The wrecker"
    }
```
- (DELETE) eliminar: http://127.0.0.1:8000/api/destroy-movie/1/

## Categories
- (POST) crear: http://127.0.0.1:8000/api/create-category/
```
    {
        "gender": "Anime"
    }

```

- (GET) listar: http://127.0.0.1:8000/api/list-category/
- (PUT) actualizar: http://127.0.0.1:8000/api/update-category/1/
```
    {
        "gender": "Cartoon"
    }
```

- (DELETE) eliminar: http://127.0.0.1:8000/api/delete-category/1/

## Reviews
- (POST)   crear: http://127.0.0.1:8000/api/review/
```
    {
        "comment": "It's amazing",
        "movie_review": "Ralph"
    }
```

- (GET)    listar: http://127.0.0.1:8000/api/review/  
- (GET)    detalle: http://127.0.0.1:8000/api/review/1/
- (PUT)    actualizar: http://127.0.0.1:8000/api/review/1/
```
    {
        "comment": "It's amazing, well, it's not is too bad."
    }
```

- (DELETE) eliminar: http://127.0.0.1:8000/api/review/1/   

## Users
- (POST) register: http://127.0.0.1:8000/api/acounts/register/
```
    {
        "email": "email@mail.com",
        "username": "username",
        "first_name": "first name",
        "password": "strong password",
        "confirm_password": "repeat strong password"
    }
```

- (POST) login: http://127.0.0.1:8000/api/acounts/login/
```
{
    "username": "username",
    "password": "strong password"
}
```

- (GET)  logout: http://127.0.0.1:8000/api/acounts/logout/

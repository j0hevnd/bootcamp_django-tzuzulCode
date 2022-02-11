from distutils.command.upload import upload
from django.db import models

# Usuarios
from django.contrib.auth.models import User

# Create your models here.

class Categorias(models.Model):
    nombre_categoria = models.CharField("Nombre categoría", max_length=100, null=False, blank=False)
    portada = models.ImageField("Portada de categoría", null=True, blank=True,
                                upload_to="categorias")
    
    class Meta:
        verbose_name="Categoria"
        verbose_name_plural="Categorias"
        
    def __str__(self):
        return self.nombre_categoria


class Articulos(models.Model):
    nombre_articulo = models.CharField("Nombre artículo", max_length=100, null=False, blank=False)
    resumen = models.CharField("Descripción artículo", max_length=150, null=False, blank=False)
    contenido = models.TextField("Contenido", null=False, blank=False)
    portada = models.ImageField("Portada de articulo", null=True, blank=True,
                                upload_to="articulos")
    slug = models.SlugField("Slug", max_length=100, unique=True, null=True, blank=True)
    categorias = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    publico = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField("Fecha de publicación", auto_now_add=True)
    fecha_edicion = models.DateTimeField("Fecha de edición", auto_now=True)
    
    class Meta:
        verbose_name="Articulo"
        verbose_name_plural="Articulos"
        
    def __str__(self):
        return self.nombre_articulo
    
    
class Comentario(models.Model):
    articulo_comentado = models.ForeignKey(Articulos, on_delete=models.CASCADE, related_name='comentarios')
    comentario = models.TextField("Comentarios", max_length=500, null=False, blank=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    creado = models.DateTimeField("Fecha de creación", auto_now=True)
    editado = models.DateTimeField("Fecha edición", auto_now_add=True)
    publico = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Comentarios"
        verbose_name_plural = "Comentarios"
        
    def __str__(self):
        return self.articulo_comentado.nombre_articulo
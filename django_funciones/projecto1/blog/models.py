from django.db import models

# Create your models here.

class Categorias(models.Model):
    nombre_categoria = models.CharField("Nombre categoría", max_length=100, null=False, blank=False)

    class Meta:
        verbose_name="Categoria"
        verbose_name_plural="Categorias"
        
    def __str__(self):
        return self.nombre_categoria


class Articulos(models.Model):
    nombre_articulo = models.CharField("Nombre artículo", max_length=100, null=False, blank=False)
    resumen = models.CharField("Descripción artículo", max_length=150, null=False, blank=False)
    contenido = models.TextField("Contenido", null=False, blank=False)
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
    
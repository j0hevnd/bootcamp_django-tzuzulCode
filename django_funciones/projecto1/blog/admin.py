from django.contrib import admin

from .models import Categorias, Articulos, Comentario
# Register your models here.

admin.site.register(Categorias)
admin.site.register(Articulos)
admin.site.register(Comentario)
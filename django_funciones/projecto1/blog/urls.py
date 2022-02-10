from django.urls import path

from . import views

app_name = "app_blog"

urlpatterns = [
    path(
        '', 
        views.index, 
        name="inicio"
    ),
    path(
        'articulo_detalle/<slug:slug>/', 
        views.detalle_articulo, 
        name="detalle"
    ),
    path(
        'articulos_categoria/<str:categoria>/', 
        views.obtener_articulos_por_categorias, 
        name="categoria"
    ),
    path(
        'eliminar-comentario/<slug:slug>/', 
        views.eliminar_comentario, 
        name="eliminar_comentario"
    ),
]
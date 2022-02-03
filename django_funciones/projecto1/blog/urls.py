from django.urls import path

from .views import index, detalle_articulo, obtener_articulos_por_categorias

app_name = "app_blog"

urlpatterns = [
    path('', index, name="inicio"),
    path('articulo_detalle/<slug:slug>/', detalle_articulo, name="detalle"),
    path('articulos_categoria/<str:categoria>/', obtener_articulos_por_categorias, name="categoria"),
]
from django.urls import path

from .views import index, detalle_articulo, obtener_articulos_por_categorias

urlpatterns = [
    path('', index),
    path('articulo_detalle/<slug:slug>/', detalle_articulo),
    path('articulos_categoria/<str:categoria>/', obtener_articulos_por_categorias),
]
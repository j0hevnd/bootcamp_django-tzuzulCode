from django.urls import path

from . import views
app_name="app_usuarios"

urlpatterns = [
    path('iniciar-sesion/', views.login_view, name='iniciar_sesion'),
    path('cerrar-sesion/', views.logout_view, name='cerrar_sesion'),
]
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'

urlpatterns = [
    # path('login/', views.LoginView.as_view(), name='login'),
    # path('logout/', views.logout_user, name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Register
    # path('register/', views.register, name='register'),
    path('register/', views.RegisterCreateView.as_view(), name='register'),
    path('register-done/', views.RegisterDoneTemplateView.as_view(), name='register_done'),
]

from django.urls import path

from apps.users import views

urlpatterns = [
    path('register/', views.RegisterCreateApiView.as_view()),
    path('login/', views.LoginApiView.as_view()),
    path('logout/', views.LogoutView.as_view()),
]

from django.urls import path

from apps.users import views

urlpatterns = [
    path('register/', views.RegisterCreateApiView.as_view()),
]

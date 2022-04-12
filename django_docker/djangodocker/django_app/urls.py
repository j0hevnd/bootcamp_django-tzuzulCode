from django.urls import path

from django_app.views import index

urlpatterns = [
    path('', index)
]

from django.urls import path

from apps.movies import views

app_name = 'app_movies'

urlpatterns = [
    path('list-category/', views.CategoryListApiView.as_view(), name='list_category'),
    path('create-category/', views.CategoryCreateApiView.as_view(), name='create_category'),
    path('update-category/<int:pk>/', views.CategoryUpdateApiView.as_view(), name='update_category'),
    path('delete-category/<int:pk>/', views.CategoryDeleteApiView.as_view(), name='delete_category'),
]

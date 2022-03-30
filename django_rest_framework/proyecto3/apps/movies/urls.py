from django.urls import path

from apps.movies import views

app_name = 'app_movies'

urlpatterns = [
    # Categories
    path('list-category/', views.CategoryListApiView.as_view(), name='list_category'),
    path('create-category/', views.CategoryCreateApiView.as_view(), name='create_category'),
    path('update-category/<int:pk>/', views.CategoryUpdateApiView.as_view(), name='update_category'),
    path('delete-category/<int:pk>/', views.CategoryDeleteApiView.as_view(), name='delete_category'),

    # Movies
    path('list-movies/', views.MovieListApiView.as_view(), name='list_movies'),
    path('create-movies/', views.MovieCreateApiView.as_view(), name='create_movies'),
    path('detail-movie/<int:pk>/', views.MovieRetrieveApiView.as_view(), name='detail_movies'),
    path('update-movie/<int:pk>/', views.MovieUpdateApiView.as_view(), name='update_movies'),
    path('destroy-movie/<int:pk>/', views.MovieDestroyApiView.as_view(), name='destroy_movies'),
]

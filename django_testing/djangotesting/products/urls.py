from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'product'

urlpatterns = [
    path("", views.ProductsListView.as_view(), name="index"),
    path("create_product/", views.ProductCreateView.as_view(), name="create_product"),
    path("detail_product/<int:pk>/", views.ProductDetailView.as_view(), name="detail_product"),
    path("edit_product/<int:pk>/", views.ProducUpdateView.as_view(), name="edit_product"),
    path("delete_product/<int:pk>/", views.ProductDeleteView.as_view(), name="delete_product"),

    #login
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    # register
    path('accounts/register/', views.RegisterCreateView.as_view(), name='register'),
    path('accounts/register-done/', views.RegisterDoneTemplateView.as_view(), name='register_done'),
]

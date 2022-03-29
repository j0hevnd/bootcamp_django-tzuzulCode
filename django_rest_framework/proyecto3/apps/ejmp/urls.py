from django.urls import path

from apps.ejmp import views

urlpatterns = [
    path('products-class/', views.ProductAPIView.as_view(), name="product_api"),
    path('products/', views.product_view_all, name="product_api"),
    path('products/<int:pk>/', views.product_detail_api_view, name="product_detail_api"),
]

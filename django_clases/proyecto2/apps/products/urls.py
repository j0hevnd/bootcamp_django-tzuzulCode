from unicodedata import name
from django.urls import path

from . import views

app_name = 'product'

urlpatterns = [
    # path('', views.home, name='index'),
    # path('', views.ProductView.as_view(), name='index'),
    # path('', views.ProductTemplateView.as_view(), name='index'),
    path('', views.ProductListView.as_view(), name='index'),
    path('detail_product/<int:pk>/', views.ProductDetailView.as_view(), name='detail_product'),
    path('create-product/', views.ProductCreateView.as_view(), name='create_product'),
    path('update-product/<int:pk>/', views.ProductUpdateView.as_view(), name='update_product'),
    path('delete-product/<int:pk>/', views.ProductDeleteView.as_view(), name='delete_product')
]

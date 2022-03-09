from django.urls import path

from . import views

app_name = 'sale'

urlpatterns = [
    path('sale_product/', views.SaleView.as_view(), name="sale_product"),
    path('add-car/', views.AddCarFormView.as_view(), name="add_car"),
    path('detail-sale/<int:pk>/', views.SaleDetailView.as_view(), name="detail_sale"),
    path('delete-sale/<int:pk>/', views.SaleDeleteView.as_view(), name="delete_sale"),
]

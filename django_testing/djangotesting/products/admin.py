from django.contrib import admin

from products.models import Product, Maker, Category
# Register your models here.

admin.site.register(Product)
admin.site.register(Maker)
admin.site.register(Category)

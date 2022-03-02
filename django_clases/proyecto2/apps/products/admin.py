from django.contrib import admin

from .models import Maker, Category, Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('added_date',)
    
    list_display = ('name_product', 'stock', 'manufacturer', 'product_type', 'product_expired', 'public')

    search_fields = (
        'name_product',
        'product_type__product_category'
    )
    list_filter = (
        'manufacturer',
        'due_date'
    )
    ordering = (
        'name_product',
        'stock'
    )
    fieldsets = [
        (None, {'fields': ['name_product', 'stock', 'price', 'manufacturer', 'product_type', 'due_date']}),
        ('Additional information', {'fields': ['added_date', 'public']})
    ]
    


# admin.site.register(Product, ProductAdmin)
admin.site.register(Maker)
admin.site.register(Category)
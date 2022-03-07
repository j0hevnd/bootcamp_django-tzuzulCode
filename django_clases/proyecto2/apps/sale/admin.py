from django.contrib import admin

from apps.sale.models import CarShop, Sale
# Register your models here.

class SaleAdmin(admin.ModelAdmin):
    readonly_fields = ('dispatch_date', 'arrival_date')

    list_display = (
        'product_to_send', 'delivery_address',
        'phone', 'paid_out', 'approved_sale', 'anulate'
    )

admin.site.register(CarShop)
admin.site.register(Sale, SaleAdmin)



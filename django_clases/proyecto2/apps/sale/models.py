from datetime import timedelta

from django.db import models
from django.utils import timezone
from django.contrib import admin

from apps.products.models import Product
# Create your models here.

class CarShop(models.Model):
    product_to_send = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField("Product quantity", null=False, blank=False)
    total_price = models.DecimalField("Total price", max_digits=10, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return f"{self.id} - {self.product_to_send}"


class Sale(models.Model):
    product_to_send = models.ForeignKey(Product, on_delete=models.CASCADE)
    delivery_address = models.CharField("Main delivery address", max_length=200, null=False, blank=False)
    delivery_address_2 = models.CharField("Second delivery address", max_length=200, null=True, blank=True)
    reference_point = models.CharField("Reference point", max_length=200, null=False, blank=False)
    phone = models.IntegerField("Main phone number", null=False, blank=False)
    phone_2 = models.IntegerField("Other phone number", null=True, blank=True)
    quantity = models.PositiveIntegerField("product quantity", null=False, blank=False)
    price_to_paid = models.DecimalField('Ammount paid', max_digits=10, decimal_places=2, null=False, blank=False)
    arrival_date = models.DateField("Arrival date", null=True, blank=True)
    dispatch_date = models.DateTimeField("dispatch date", null=True, blank=True)
    paid_out = models.BooleanField('Paid out?', default=False)
    approved = models.BooleanField('Approved?', default=False)
    anulate = models.BooleanField("Sale cancelled?", default=False)

    class Meta:
        verbose_name = "Sale"
        verbose_name_plural = "Sales"

    @admin.display(
        boolean= True,
        description="Approved?"
    )
    def approved_sale(self):
        if self.approved and self.dispatch_date is None:
            self.dispatch_date = timezone.now()
            self.arrival_date = timezone.now() + timedelta(4)
            self.save()

        if not self.approved and self.dispatch_date is not None:
            self.dispatch_date = None
            self.arrival_date = None
            self.save()

        return self.approved


    def __str__(self):
        return f"{self.id} - {self.product_to_send}"
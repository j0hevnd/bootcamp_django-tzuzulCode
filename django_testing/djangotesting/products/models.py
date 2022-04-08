from django.db import models
from django.contrib import admin
from django.utils import timezone

# Create your models here.

class Maker(models.Model):
    """ Modelo que representará una tabla de un fabricante en la base de datos """

    manufacturer_name = models.CharField("Maker", max_length=200, null=False, blank=False)

    class Meta:
        verbose_name = 'Maker'
        verbose_name_plural = 'Makers'

    def __str__(self):
        return f"{self.id} - {self.manufacturer_name}"


class Category(models.Model):
    """ Modelo que representa una categoria de productos en la base de datos """

    product_category = models.CharField("Kind of product", max_length=100, null=False, blank=False)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f"{self.id} - {self.product_category}"


class Product(models.Model):
    """ Modelo que representa un producto en la base de datos """

    name_product = models.CharField("Name product", max_length=200, unique=True, null=False, blank=False)
    stock = models.IntegerField("Stock available ", default=0)
    price = models.FloatField("Price", default=00.0)
    manufacturer = models.ForeignKey(Maker, on_delete=models.CASCADE)
    product_type = models.ForeignKey(Category, on_delete=models.CASCADE)
    due_date = models.DateTimeField("Due date", null=False, blank=False)
    added_date = models.DateTimeField("Added date", auto_now_add=True)
    public = models.BooleanField("Public?", default=True)
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['id']

    @admin.display( 
        boolean=True,
        description="expired product?" 
    ) 
    def product_expired(self):
        """ funcion para validar atributos del base de datos """
        due_date = self.due_date < timezone.now()
        if due_date and self.public: 
            self.public = False
            self.save()
        elif not due_date and not self.public and self.stock > 0:
            self.public = True
            self.save()
        return due_date

    def __str__(self):
        return self.name_product


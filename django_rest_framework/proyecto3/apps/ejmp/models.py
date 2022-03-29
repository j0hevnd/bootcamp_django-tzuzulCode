from django.db import models

# Create your models here.

class Product(models.Model):
    """ Model that represents a product in the database """
    name_product = models.CharField("Product name", unique=True, max_length=200, null=False, blank=False)
    stock = models.IntegerField("Stock available", default=0)
    price = models.FloatField("Price", default=00.0)
    added_date = models.DateTimeField("Added date", auto_now_add=True)
    public = models.BooleanField("Public?", default=True)    

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
    def __str__(self):
        return self.name_product

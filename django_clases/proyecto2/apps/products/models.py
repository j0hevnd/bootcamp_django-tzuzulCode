from django.db import models
from django.contrib import admin
from django.utils import timezone

# Create your models here.

class Maker(models.Model):
    """ Model that represents a table of a manufacturer in the database """
    manufacturer_name = models.CharField("Marker", max_length=200, null=False, blank=False)

    class Meta:
        """ Metadata that we specify for the model """
        verbose_name = "Maker"
        verbose_name_plural = "Makers"

    def __str__(self):
        """ Representation that we give to the model, both in the admin and for queries """
        return self.manufacturer_name


class Category(models.Model):
    """ Model representing a category of products in the database """
    product_category = models.CharField("kind of product", max_length=100, null=False, blank=False)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.product_category


class Product(models.Model):
    """ Model that represents a product in the database """
    name_product = models.CharField("Product name", unique=True, max_length=200, null=False, blank=False)
    image_product = models.ImageField('Image product', upload_to='product/', null=False, blank=False)
    stock = models.IntegerField("Stock available", default=0)
    price = models.FloatField("Price", default=00.0)
    manufacturer = models.ForeignKey(Maker, on_delete=models.CASCADE)
    product_type = models.ForeignKey(Category, on_delete=models.CASCADE)
    due_date = models.DateTimeField("Due date", null=False, blank=False)
    added_date = models.DateTimeField("Added date", auto_now_add=True)
    public = models.BooleanField("Public?", default=True)    

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    @admin.display(
        boolean=True,
        description='Expired product?'
    )
    def product_expired(self):
        """ function to validate database attributes """
        product_expired = self.due_date < timezone.now()

        if (product_expired and self.public) or self.stock == 0:
            self.public = False
            self.save()

        elif not product_expired and not self.public and self.stock > 0:
            self.public = True
            self.save()

        return product_expired
    
    def __str__(self):
        return self.name_product
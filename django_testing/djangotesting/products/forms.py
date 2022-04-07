from datetime import timedelta

from django import forms
from django.utils import timezone, dateformat

from .models import Product


formatted_date = dateformat.format(timezone.now(), 'Y-m-d H:i')

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name_product', 'stock', 'price', 'manufacturer', 'product_type', 'due_date']
        labels = {
            'name_product': 'Name of product',
            'stock': 'Quantity',
            'price': 'Price',
            'manufacturer': 'Maker',
            'product_type': 'Kind of product',
            'due_date': 'Due date',
        }
        
        widgets = {
            'name_product': forms.TextInput(
                attrs= {
                    'placeholder': 'Product name'
                }
            ),
            'stock': forms.NumberInput(
                attrs= {
                    'min': '1',
                    'max': '100'
                }
            ),
            'price': forms.NumberInput(
                attrs= {
                    'min':'0',
                }
            ),
            'manufacturer': forms.Select(),
            'product_type': forms.Select(),
            'due_date': forms.DateTimeInput(
                attrs= {
                    'type': 'datetime-local',
                }
            )
        }

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 1:
            self.add_error('price', 'The price must be greater than 0')
        return price

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date < (timezone.now() + timedelta(10)):
            self.ValidationError('Due date must be greater than 10 days after today', code='invalid')
        return due_date

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock < 1 or stock > 100:
            raise forms.ValidationError('Enter a number greater than 0 and less than 100', code='invalid')
        return stock
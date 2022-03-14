from django import forms

from apps.products.models import Product
from .models import Sale, CarShop


class AddCarForm(forms.Form):
    """ Create custom form fields """
    quantity = forms.IntegerField(
        required = True,
        # min_value = 1,
        # max_value = 10,
        widget = forms.NumberInput(
            attrs = {
                'value': '1'
            } 
        )
    ) 

    # validate
    def clean_quantity(self):
        """ Validate form fields """
        quantity = self.cleaned_data.get('quantity')
        if quantity < 1 or quantity > 10:
            raise forms.ValidationError('Enter a quantity greater than 0 and less than 10', code='invalid')
        
        return quantity


class SaleForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        """ We assign our own information to one of the fields that this form represents """
        super().__init__(*args, **kwargs)

        self.fields['product_to_send'].queryset = Product.objects.filter(
            public=True,
            stock__gt = 0
        )


    class Meta:
        model = Sale 
        fields = ('delivery_address', 'delivery_address_2', 'reference_point',
                  'phone', 'phone_2', 'product_to_send', 'quantity')


    def clean(self):
        """ We do different validations to form fields, we add each error
        to its respective field via the method add_error(field, message)
        
        return: All data sent.
        """
        cleaned_data = super().clean()
        phone = str(cleaned_data.get('phone'))
        phone_2 = str(cleaned_data.get('phone_2'))

        if len(phone) < 7 or len(phone) > 10:
            self.add_error('phone', 'The entered number must have 7 to 10 numbers') 
        
        if len(phone_2) < 7 or len(phone_2) > 10:
            self.add_error('phone_2', 'The entered number must have 7 to 10 numbers') 

        if phone == phone_2:
            self.add_error('phone_2', 'Must be a different phone number that the first')

        return cleaned_data

    def clean_delivery_address_2(self):
        """
        Validate specified field after word clean_
        Return: Field validated
        """
        address = self.cleaned_data['delivery_address']
        address_2 = self.cleaned_data['delivery_address_2']

        if address == address_2:
            raise forms.ValidationError('Must be a different address that the first', code='invalid')

        return address_2


    def clean_quantity(self):
        """
        Validate specified field after word clean_
        Return: Field validated
        """
        quantity = self.cleaned_data['quantity']
        product = self.cleaned_data['product_to_send']

        if quantity > product.stock:
            message = f'The quantity ordered is most than the quantity in stock. Count in stock: {product.stock }'
            raise forms.ValidationError(message, code='invalid')
        
        return quantity
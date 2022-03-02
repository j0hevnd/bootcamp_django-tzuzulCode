from multiprocessing.sharedctypes import Value
from django import forms

from .models import Sale, CarShop


class AddCarForm(forms.Form):
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
        quantity = self.cleaned_data.get('quantity')
        if quantity < 1 or quantity > 10:
            raise forms.ValidationError('Enter a quantity greater than 0 and less than 10', code='invalid')
        
        return quantity


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale 
        fields = ('delivery_address', 'delivery_address_2', 'reference_point',
                  'phone', 'phone_2', 'product_to_send', 'quantity')


    def clean(self):
        cleaned_data = super().clean()
        phone = str(cleaned_data.get('phone'))
        phone_2 = str(cleaned_data.get('phone_2'))

        if len(phone) < 7 or len(phone) > 10:
            self.add_error('phone', 'The entered number must have 7 to 10 numbers') 
        
        if len(phone_2) < 7 or len(phone_2) > 10:
            self.add_error('phone_2', 'The entered number must have 7 to 10 numbers') 

        if phone == phone_2:
            self.add_error('phone_2', 'Must be a different phone number that the first')


    def clean_delivery_address_2(self):
        address = self.cleaned_data['delivery_address']
        address_2 = self.cleaned_data['delivery_address_2']

        if address == address_2:
            raise forms.ValidationError('Must be a different address that the first', code='invalid')
        
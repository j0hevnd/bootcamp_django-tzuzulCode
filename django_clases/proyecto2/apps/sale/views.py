from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views.generic import View
from django.views.generic.edit import FormView

from apps.products.models import Product
from .models import CarShop, Sale
from .forms import AddCarForm, SaleForm


# Create your views here.

class SaleView(View):
    def get(self, request, *args, **kwargs):
        query_sale = Sale.objects.all()
        
        return render(
            request, 
            'sale/sale_list.html', 
            {'products':query_sale}
        ) 

    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('id_product')
        shipment = get_object_or_404(Sale, pk=product_id)

        return HttpResponseRedirect(reverse('sale:sale_product'))


class AddCarFormView(FormView):
    template_name = 'sale/sale_form.html'
    form_class = SaleForm
    success_url = reverse_lazy('product:index')

    def form_valid(self, form):
        count = form.cleaned_data.get('quantity')
        product_to_send = form.cleaned_data.get('product_to_send')
        total_price = product_to_send.price * count

        try:
            obj, created = Sale.objects.get_or_create(
                quantity=count,
                price_to_paid = total_price,
                defaults = {
                    **form.cleaned_data
                }
            )
            
        except Exception as e:
            print("An error has ocurred due to....", e)

        return super(AddCarFormView, self).form_valid(form)

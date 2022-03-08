from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import View, DeleteView
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404

from apps.products.models import Product
from .models import CarShop, Sale
from .forms import AddCarForm, SaleForm


# Create your views here.

class SaleView(View):
    def get(self, request, *args, **kwargs):
        query_sale = Sale.objects.all()

        query_sale_send = list(filter(lambda sale: not sale.paid_out \
            and not sale.anulate, 
            query_sale)
        )
        shipments_by_approval = list(filter(lambda sale: sale.paid_out \
            and not sale.approved \
            and not sale.anulate, \
            query_sale)
        )
        approved_shipments = list(filter(lambda sale: sale.approved \
            and not sale.anulate \
            and sale.dispatch_date \
            and sale.arrival_date, \
            query_sale)
        )
        cancelled_shipments = list(filter(lambda sale: sale.anulate, query_sale))

        return render(
            request, 
            'sale/sale_list.html', 
            {
                'products':query_sale_send,
                'shipments_by_approval': shipments_by_approval,
                'approved_shipments': approved_shipments,
                'cancelled_shipments': cancelled_shipments,
            }
        ) 

    def post(self, request, *args, **kwargs):
        shipment = get_object_or_404(Sale, pk=request.POST.get('id_product'))
        shipment.paid_out = True
        shipment.save()

        return HttpResponseRedirect(reverse('sale:sale_product'))


class AddCarFormView(FormView):
    """
    
    """
    template_name = 'sale/sale_form.html'
    form_class = SaleForm
    success_url = reverse_lazy('product:index')

    def form_valid(self, form):
        """
        """
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
            
            if created:
                obj.product_to_send.stock -=count
                product_to_send.save()

        except Exception as e:
            print("An error has ocurred due to....", e)

        return super(AddCarFormView, self).form_valid(form)


class SaleDeleteView(DeleteView):
    model = Sale
    success_url = reverse_lazy('sale:sale_product')
    
    def post(self, request, pk, *args, **kwargs):
        object = self.model.objects.get(id=pk)
        object.product_to_send.stock += object.quantity
        object.product_to_send.save()
        object.delete()
        return redirect(self.success_url)
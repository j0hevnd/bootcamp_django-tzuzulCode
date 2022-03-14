from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import View, DetailView, DeleteView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.products.models import Product
from .models import Sale
from .forms import SaleForm


# Create your views here.

class SaleView(LoginRequiredMixin, View):
    model = Sale
    template_name = 'sale/sale_list.html'

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        query_sale = self.get_queryset()
        context = {}

        context["query_sale_send"] = list(filter(lambda sale: not sale.paid_out \
            and not sale.anulate, 
            query_sale)
        )
        context["shipments_by_approval"] = list(filter(lambda sale: sale.paid_out \
            and not sale.approved \
            and not sale.anulate, \
            query_sale)
        )
        context["approved_shipments"] = list(filter(lambda sale: sale.approved \
            and not sale.anulate \
            and sale.dispatch_date \
            and sale.arrival_date, \
            query_sale)
        )
        context["cancelled_shipments"] = list(filter(lambda sale: sale.anulate, query_sale))

        return context
    
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())


    def post(self, request, *args, **kwargs):
        shipment = get_object_or_404(Sale, pk=request.POST.get('id_product'))
        shipment.paid_out = True
        shipment.save()

        return HttpResponseRedirect(reverse('sale:sale_product'))


class AddCarFormView(LoginRequiredMixin, FormView):
    """
    
    """
    template_name = 'sale/sale_form.html'
    form_class = SaleForm
    success_url = reverse_lazy('product:index')

    def form_valid(self, form):
        """
        """
        count = form.cleaned_data.pop('quantity')
        product_to_send = form.cleaned_data.get('product_to_send')
        total_price = product_to_send.price * count

        try:
            # get_or_create()
            sale_create = Sale.objects.create( # Sale
                quantity = count,
                price_to_paid = total_price,
                **form.cleaned_data
            )
            sale_create.product_to_send.stock -= count # Sale / Product

            sale_create.product_to_send.save() # Product.save()
            sale_create.save() # Sale.save()

        except Exception as e:
            print("An error has ocurred due to....", e)

        return super(AddCarFormView, self).form_valid(form)


class SaleDetailView(LoginRequiredMixin, DetailView):
    model = Sale


class SaleDeleteView(LoginRequiredMixin, DeleteView):
    model = Sale
    success_url = reverse_lazy('sale:sale_product')
    
    def post(self, request, pk, *args, **kwargs):
        object = self.model.objects.get(id=pk)
        object.product_to_send.stock += object.quantity
        object.product_to_send.save()
        object.delete()
        return redirect(self.success_url)
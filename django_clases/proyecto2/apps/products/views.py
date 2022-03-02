from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    View, 
    TemplateView, 
    ListView,
    DetailView,
    CreateView, 
    UpdateView,
    DeleteView
)

from .models import Product
from .forms import ProductForm
from apps.sale.forms import AddCarForm

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, "list.html", {'products':products})

# dispacth()

class ProductView(View):

    def get(self, request, *args, **kwargs):
        # .....
        products = Product.objects.all()
        return render(request, "list.html", {'products':products})

    def post(self, request, *args, **kwargs):
        print("Inside the post() method")
        return self.get(request)


class ProductTemplateView(TemplateView, ProductView):
    template_name = 'base.html'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ProductListView(ListView):
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    # queryset = Product.objects.all()
    # ordering = '-price'

    def get_queryset(self):
        products = Product.objects.filter(public=True).order_by('-price')
        queryset = [product for product in products if not product.product_expired()]
        return queryset


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AddCarForm
        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product:index')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product:index')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product:index')

    def post(self, pk):
        product = self.model.objects.get(id=pk)
        product.public = False
        product.save()
        return redirect(self.success_url)
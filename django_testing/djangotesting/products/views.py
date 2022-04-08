from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView, 
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin

from products.models import Product
from products.forms import ProductForm


class ProductsListView(LoginRequiredMixin, ListView):
    """ 
    Clase para listar del base de datos 
    Le pasamos variables de clase propias como:
    """
    template_name = "product/list.html"
    context_object_name = 'products'
    paginate_by = 8 # page_obj   

    def get_queryset(self):
        """
        Lo sobreescribimos para hacer consultas más complejas que usarán nuestros templates.
        Si usamos este ya no es necesario usar la varible 'queryset'.

        return: Resultado de una consulta a base de datos.
        """
        products = Product.objects.filter(
            public=True,
            stock__gt=0
        )

        products = list(filter(lambda product: not product.product_expired(), products))
        
        return products


class ProductDetailView(LoginRequiredMixin, DetailView):
    """
    Clase para ver el detalle de un producto. 
    """
    model = Product
    template_name = "product/product_detail.html"

    def get_object(self):
        queryset = self.get_queryset().filter(public=True, stock__gt=0)
        try:
            return queryset.get()
        except queryset.model.DoesNotExist:
            return None


class ProductCreateView(LoginRequiredMixin, CreateView):
    """ 
    Vista para crear un objeto en la base de datos.
    """
    model = Product
    template_name = "product/create_product.html"
    form_class = ProductForm
    success_url = reverse_lazy('product:index')


class ProducUpdateView(LoginRequiredMixin, UpdateView):
    """ 
    Vista para actualizar un objeto de la base de datos
    """
    model = Product
    template_name = "product/create_product.html"
    form_class = ProductForm
    success_url = reverse_lazy('product:index')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """ 
    Vista para eliminar un elemento de la base de datos
    """
    model = Product
    template_name='product/product_confirm_delete.html'
    success_url = reverse_lazy('product:index')

    def post(self, request, pk, *args, **kwargs):
        """ 
        Sobreescribimos el método 'post' que implementa internamente para 
        para hacer manejo de propia lógica.
        
        return: HTTPResponse con la ruta a dirigir. 
        """
        object = self.model.objects.get(id=pk)
        object.public = False
        object.save()
        return redirect('product:index')


# Users register
from django.contrib.auth.forms import UserCreationForm

class RegisterCreateView(CreateView):
    """ Registro de usuario """
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy("user:register_done")


class RegisterDoneTemplateView(TemplateView):
    """ Muestra un template de éxito cuando registramos correctamente un usuario """
    template_name = 'registration/register_done.html' 
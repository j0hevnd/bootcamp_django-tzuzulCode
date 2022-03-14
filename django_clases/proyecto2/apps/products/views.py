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
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Product
from .forms import ProductForm
from apps.sale.forms import AddCarForm

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, "list.html", {'products':products})

"""
class-based views do internal handling of methods to validate requests that
are made from a client, some are:
    - dispatch() : Validates the HTTP method of the request to make use of the correct function
    which handles the type of request sent.
    - http_method_not_allowed() : if information is sent by an unsupported HTTP method, it is executed
    this method

(there's a couple more)
"""

class ProductView(View):
    """
    View, 'parent' view from which all other class-based views inherit.
    We use it to write logic, for this we override some of its methods:
    POST, GET, DELETE... We can also use some other methods of VBC
    for behavior management.
    """

    def get(self, request, *args, **kwargs):
        """ Receives the GET method that is sent from the browser """
        # .....
        products = Product.objects.all()
        return render(request, "list.html", {'products':products})

    def post(self, request, *args, **kwargs):
        """ Receives the POST method that is sent from the browser """
        print("Inside the post() method")
        return self.get(request)


class ProductTemplateView(TemplateView, ProductView):
    """ Class-based view that we mainly use to render a template"""
    template_name = 'base.html'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ProductListView(ListView):
    """
    Class to list the database
    We pass it our own class variables like:

        - model : class that specifies our table in the database
        - template_name : HTML file path that template as it will be displayed
          information.
        - queryset : query to the database.
        - context_object_name : name with which we send the results of
          the query to our template.
    
    Among other; these are the most used. Most classes require at least the 'model'
    and the 'template_name'
    
    Like other class-based views, we can override methods like:
        -get()
        - get_queryset()
        - get_context_data()
    """
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 5
    # queryset = Product.objects.all()
    # ordering = '-price'

    def get_queryset(self):
        products = Product.objects.filter(
            public=True,
            stock__gt = 0
        ).order_by('-price')
        # queryset = [product for product in products if not product.product_expired()]
        return products


class ProductDetailView(DetailView):
    """
    Class to see the detail of a product. This gets a 'pk' or 'slug' as a parameter
    that has been specified in the URLs.
    Requires the 'model' parameter, that way you will know where to look for the object detail
    passed by URL.
    We can also override VBC's own methods
    """
    model = Product

    def get_context_data(self, **kwargs):
        """ Send variables as contexts to the template to be used there """
        context = super().get_context_data(**kwargs)
        context['form'] = AddCarForm
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    """
    View to create an object in the database.
    Requires:
        - model
        - form_class : a form to render to the client
        - template_name (if you don't pass your own, it looks for one by default)
        - success_url : URL where it will redirect if everything goes correctly
    """
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product:index')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """
    View to update a database object.
    It requires an attribute, be it 'pk' or 'slug' to know which element it refers to
    It is handled similar to DetailView.
    """
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product:index')


class ProductDeleteView(LoginRequiredMixin, DeleteView): 
    """
    View to delete an item from the database.
    It is handled similar to UpdateView.
    """
    model = Product
    success_url = reverse_lazy('product:index')

    def post(self, pk):
        """
        We override the 'post' method that it implements internally to
        to handle your own logic.
        
        return: HTTPResponse with the route to direct.
        """
        product = self.model.objects.get(id=pk)
        product.public = False
        product.save()
        return redirect(self.success_url)
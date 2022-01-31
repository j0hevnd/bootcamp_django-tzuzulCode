from django.http import HttpResponse
from django.shortcuts import render

# models
from .models import Articulos

# Create your views here.
def index(request):
    articulos = Articulos.objects.all()
    context = {
        'articulos': articulos
    }
    return render(request=request, template_name="index.html", context=context)


def obtener_articulos_por_categorias(request, categoria):
    articulos = Articulos.objects.filter(
        categorias__nombre_categoria = categoria
    )
    
    return render(request, "articulos_categoria.html", {'articulos': articulos})


def detalle_articulo(request, pk):
    articulo = Articulos.objects.get(id=pk)
    return render(request, "detalle.html", {'articulo': articulo})

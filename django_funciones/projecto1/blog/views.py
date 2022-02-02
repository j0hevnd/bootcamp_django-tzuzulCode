from django.http import HttpResponse
from django.shortcuts import render

# models
from .models import Articulos

# Create your views here.
def index(request):
    articulos = Articulos.objects.filter(
        publico = True
    )
    
    context = {
        'articulos': articulos
    }
    return render(request=request, template_name="index.html", context=context)


def obtener_articulos_por_categorias(request, categoria):
    articulos = Articulos.objects.filter(
        publico = True,
        categorias__nombre_categoria = categoria
    )
    
    return render(request, "articulos_categoria.html", {'articulos': articulos})


def detalle_articulo(request, slug):
    context = {}
    try:
        articulo = Articulos.objects.get(slug=slug)
        if articulo is not None:
            context['articulo'] = articulo
            return render(request, "detalle.html", context)
        
    except Articulos.DoesNotExist:
        context['msj_error'] = "Articulo no encontrado"
        return render(request, "detalle.html", context)
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.db.models import Q

# models
from .models import Articulos, Categorias, Comentario

# Create your views here.


def consulta_busqueda(argumento_busqueda, categoria):
    if categoria is not None:
        consulta = Articulos.objects.filter(
            Q(nombre_articulo__icontains=argumento_busqueda) |
            Q(resumen__icontains=argumento_busqueda),
            publico = True,
            categorias__nombre_categoria = categoria,
        ) 
    
    else:
        consulta = Articulos.objects.filter(
            Q(nombre_articulo__icontains=argumento_busqueda) |
            Q(resumen__icontains=argumento_busqueda),
            publico = True
        ) 

    if consulta is not None:
        return consulta
        
    return False
    
def busqueda(request, context):
    
    obtener_categoria = None
    busqueda = request.GET.get('buscar')
    
    if len(request.path.split("/")) > 2:
        obtener_categoria = request.path.split("/")[2]
    
    articulos_encontrados = consulta_busqueda(busqueda, obtener_categoria)
    
    if articulos_encontrados:
        context['articulos'] = articulos_encontrados
        return context

    else:
        context['msj_no_encontrado'] = "No se encontraron coincidencias con \"%s\" " % busqueda
    
    return context


def index(request):
    articulos = Articulos.objects.filter(
        publico = True
    )

    context = {
        'articulos': articulos
    }
    
    if request.GET.get('buscar'):
        busqueda(request, context)
    
    return render(request=request, template_name="index.html", context=context)


def obtener_articulos_por_categorias(request, categoria):
    context = {}
    
    try:
        categoria = Categorias.objects.get(nombre_categoria=categoria)
        
        articulos = Articulos.objects.filter(
            publico = True,
            categorias__nombre_categoria = categoria
        )
        
        context['articulos'] = articulos
        context['categoria'] = categoria
        
        if request.GET.get('buscar'):
            busqueda(request, context)
        
        if articulos:
            return render (request, "articulos_categoria.html", context)
        
        context['no_datos'] = "Pronto agregaremos contenido! :)"
        
    except Categorias.DoesNotExist:
        context['contenido_404'] = "Esta categoría no existe"

    return render (request, "articulos_categoria.html", context)


def detalle_articulo(request, slug):
    context = {}
    try:
        articulo = Articulos.objects.get(slug=slug)
        comentarios = articulo.comentarios.all()
        context['articulo'] = articulo
        
        if comentarios: context['comentarios'] = comentarios
        else: context['no_comentarios'] = "¡Sé el primero en comentar!"
        
        comentario = None
        if request.GET.get("editar") and request.user.is_authenticated:
            comentario = comentarios.get(id=request.GET.get("editar"))
            context['comentario'] = comentario.comentario
            context['path'] = request.get_full_path
        
        if request.method == 'POST':
            if not request.user.is_authenticated:
               return redirect('app_usuarios:iniciar_sesion') 

            comentario_nuevo = request.POST.get("comentario").strip()
            
            if comentario_nuevo and not comentario:
                try:
                    Comentario.objects.create(
                        comentario = comentario_nuevo,
                        articulo_comentado = articulo,
                        usuario = request.user
                    )
                except Exception as e:
                    raise Http404(f"Hubo un error debido a.... {e}")

                return HttpResponseRedirect(request.path)
            
            elif comentario_nuevo and comentario:
                comentario.comentario = comentario_nuevo
                comentario.save()
                
            else:
                context['comentario_error'] = "El comentario no puede ir vacio"
                
                
    except Articulos.DoesNotExist:
        context['msj_error'] = "Artículo no encontrado"
    
    return render(request, "detalle.html", context)
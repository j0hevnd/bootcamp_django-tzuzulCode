from .models import Categorias

def obtener_categorias(request):
    categorias = Categorias.objects.all()
    
    return {
        'categorias': categorias,
    }
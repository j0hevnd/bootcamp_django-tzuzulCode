from audioop import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

from .forms import FormularioRegistro
# Create your views here.


def regitrar_usuario(request):
    if request.user.is_authenticated:
        return redirect('app_blog:inicio')
    
    if request.method == 'POST':
        formulario_registro = FormularioRegistro(request.POST)

        if formulario_registro.is_valid():
            formulario_registro.save()
            return redirect("app_usuarios:iniciar_sesion")
        
    else:
        formulario_registro = FormularioRegistro()
        
    context = {
        'formulario': formulario_registro
    }
    
    return render(request, "usuarios/registro.html", context)


def login_view(request):
    
    if request.user.is_authenticated:
        return redirect('app_blog:inicio')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('app_blog:inicio')
        
        context = {'msj_error': "Nombre de usuario o contraseña inválidos"}
        return render(request, "usuarios/login.html", context)
    
    return render(request, "usuarios/login.html")

def logout_view(request):
    logout(request)
    return redirect("app_usuarios:iniciar_sesion")
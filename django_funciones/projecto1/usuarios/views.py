from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
# Create your views here.


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
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.views.generic import CreateView, TemplateView
from django.contrib.auth import login, logout

from .forms import LoginForm, UserRegistrationForm
# Create your views here.

class LoginView(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('product:index')

    @method_decorator(never_cache)
    @method_decorator(csrf_protect)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super().dispatch(request, *args, **kwargs)


    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)

# def logout_user(request):
#     logout(request)
#     return redirect(reverse('users:login'))

def register(request):
    if request.method=="POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/register_done.html')

    else: 
        user_form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': user_form})


class RegisterCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy("users:register_done")

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.set_password(self.request.POST['password'])
        return super().form_valid(form)


class RegisterDoneTemplateView(TemplateView):
    template_name = 'registration/register_done.html'
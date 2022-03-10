from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth import login, authenticate

from .forms import LoginForm
# Create your views here.

class LoginView(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('product:index')

    def form_valid(self, form):
        login(self.request, form.cleaned_data['username'],)
        return super().form_valid(form)
        render ()

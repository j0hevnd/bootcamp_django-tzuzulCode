from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    username='Jhon'
    to='TzuzulCode bootcamp'
    return render(request=request, template_name='index.html', context={'username':username, 'to':to})

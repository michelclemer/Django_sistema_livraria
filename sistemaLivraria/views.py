from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.


def inicio(request):
    return HttpResponse("<h1> Bem vindo a Biblioteca</h1>")


def about(request):
    return render(request, 'paginas/about.html')
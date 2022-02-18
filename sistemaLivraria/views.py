from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.


def inicio(request):
    return render(request, 'paginas/inicio.html')
def about(request):
    return render(request, 'paginas/about.html')


def livros(request):
    return render(request, 'livros/index.html')
def criar(request):
    return render(request, 'livros/criar.html')
from django.shortcuts import render
from django.http import HttpResponse
from .models import Livro


# Create your views here.


def inicio(request):
    return render(request, 'paginas/inicio.html')
def about(request):
    return render(request, 'paginas/about.html')


def livros(request):
    livros = Livro.objects.all()
    print(livros)
    return render(request, 'livros/index.html', {'livros': livros})
def criar(request):
    return render(request, 'livros/criar.html')
def editar(request):
    return render(request, 'livros/editar.html')
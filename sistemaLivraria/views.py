from urllib.request import Request
from django.shortcuts import render
from django.http import HttpResponse
from .models import Livro
from .forms import LivroForm

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
    formulario = LivroForm(request.POST or None)
    return render(request, 'livros/criar.html', {'formulario': formulario})

def editar(request):
    return render(request, 'livros/editar.html')
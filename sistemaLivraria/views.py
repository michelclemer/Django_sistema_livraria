from urllib.request import Request
from django.shortcuts import render, redirect
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
    formulario = LivroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('livros')
    return render(request, 'livros/criar.html', {'formulario': formulario})

def editar(request,id):
    livro = Livro.objects.get(id=id)
    formulario = LivroForm(request.POST or None, request.FILES or None, instance=livro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('livros')
    return render(request, 'livros/editar.html', {'formulario': formulario})

def deletar(request, id):
    livro = Livro.objects.get(id=id)
    livro.delete()
    return redirect('livros')
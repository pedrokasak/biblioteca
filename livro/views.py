from django.http import request
from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist
from .forms import AutorForm, LivroForm
from .models import Autor, Livro

# Create your views here.


def Home(req):
    return render(req, 'index.html')


def CriarAutor(request):
    if request.method == 'POST':
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save()
            return redirect('livro:listar_autor')
    else:
        autor_form = AutorForm()
    return render(request, 'livro/criar_autor.html', {'autor_form': autor_form})


def listarAutor(request):
    autores = Autor.objects.filter(estado=True)
    return render(request, 'livro/listar_autor.html', {'autores': autores})


def editarAutor(request, pk):
    autor_form = None
    error = None
    try:
        autor = Autor.objects.get(pk=pk)
        if request.method == 'GET':
            autor_form = AutorForm(instance=autor)
        else:
            autor_form = AutorForm(request.POST, instance=autor)
            if autor_form.is_valid():
                autor_form.save()
                return redirect('index')
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'livro/criar_autor.html', {'autor_form': autor_form, 'error': error})


def excluiAutor(request, pk):
    autor = Autor.objects.get(pk=pk)
    # autor.delete()
    if request.method == 'POST':
        autor.estado = False
        autor.save()
        return redirect('livro:listar_autor')
    return render(request, 'livro/excluir_autor.html', {'autor': autor})


def listarLivro(request):
    livro = Livro.objects.all()
    return render(request,'livro/listar_livro.html',{'livro':livro})


def CadastrarLivro(request):
    if request.method == 'POST':
        livro_form = LivroForm(request.POST)
        if livro_form.is_valid():
            livro_form.save()
            return redirect('index')
    else:
        livro_form = LivroForm()
    return render(request, 'livro/criar_livro.html', {'livro_form': livro_form})


def editarLivro(request, pk):
    livro = Livro.objects.get(pk=pk)
    form = LivroForm(request.POST, instance=livro)
    if request.method == 'POST':
        livro.save()
        return redirect('livro:listar_livro')
    return render(request,'livro/editar_livro.html',{'livro':livro,'form':form})


def excluirLivro(request, pk):
    livro = Livro.objects.get(pk=pk)
    if request.method == 'POST':
        livro.delete()
        livro.save()
        return redirect('livro:listar_livro')
    return render(request, 'livro/excluir_livro.html', {'livro': livro})

from django.urls import path
from .views import CriarAutor, excluiAutor, listarAutor, editarAutor, CadastrarLivro, listarLivro

urlpatterns = [
    path('criar_autor/', CriarAutor, name='criar_autor'),
    path('listar_autor/', listarAutor, name='listar_autor'),
    path('editar_autor/<int:id>', editarAutor, name='editar_autor'),
    path('excluir_autor/<int:id>', excluiAutor, name='excluir_autor'),


    path('listar_livro/<int:id>', listarLivro, name='listar_livro'),
    path('cadastrar_livro/', CadastrarLivro, name='cadastrar_livro'),
    path('editar_livro/<int:id>', excluiAutor, name='editar_livro'),
    path('excluir_livro/<int:id>', excluiAutor, name='excluir_livro'),


]
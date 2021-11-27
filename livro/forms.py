from django import forms
from django.forms import fields
from .models import Autor, Livro

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome','nacionalidade','descricao']


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = '__all__'
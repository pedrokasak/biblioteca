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
        
        fields = ['titulo','data_publicacao','editora','autor_id']
        
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'data_publicacao': forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'editora': forms.TextInput(attrs={'class':'form-control'}),
            'autor_id': forms.Select(attrs={'class':'form-control'}),
        }
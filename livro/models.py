from django.db import models

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=60,blank=False, null=True)
    nacionalidade = models.CharField(max_length=30, blank=False, null=True)
    descricao = models.TextField(blank=False, null=True)
    estado = models.BooleanField('Estado', default=True)
    data_criacao = models.DateTimeField('Data de Criação', auto_now=True , auto_now_add=False)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Livro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo', max_length=100,blank=False, null=False)
    data_publicacao = models.DateField('Data de Publicação', blank=False, null=False)
    autor_id = models.ManyToManyField(Autor)
    data_criacao = models.DateTimeField('Data de  Criação', auto_now=True, auto_now_add=False)
    editora = models.CharField('Editora', max_length=50,blank=False, null=False)

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo

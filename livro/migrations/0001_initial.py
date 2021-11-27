# Generated by Django 3.2.9 on 2021-11-01 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=60, null=True)),
                ('nacionalidade', models.CharField(max_length=30, null=True)),
                ('descricao', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='livro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('data_publicacao', models.DateField(verbose_name='Data de Publicação')),
                ('autor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livro.autor')),
            ],
            options={
                'verbose_name': 'Livro',
                'verbose_name_plural': 'Livros',
                'ordering': ['titulo'],
            },
        ),
    ]

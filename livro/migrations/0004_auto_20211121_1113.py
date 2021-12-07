# Generated by Django 3.2.9 on 2021-11-21 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0003_auto_20211102_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='editora',
            field=models.CharField(default=1, max_length=50, verbose_name='Editora'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='livro',
            name='fecha_criacao',
            field=models.DateTimeField(auto_now=True, verbose_name='Data de  Criação'),
        ),
    ]
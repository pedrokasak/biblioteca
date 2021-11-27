# Generated by Django 3.2.9 on 2021-11-02 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0002_auto_20211101_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='data_criacao',
            field=models.DateTimeField(auto_now=True, verbose_name='Data de Criação'),
        ),
        migrations.AddField(
            model_name='autor',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
    ]

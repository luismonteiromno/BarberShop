# Generated by Django 4.0.1 on 2024-05-06 12:22

import django_editorjs.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_servico', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome do serviço')),
                ('descricao', django_editorjs.fields.EditorJsField(blank=True, help_text='Você também pode adicionar imagens na descrição', null=True, verbose_name='Descrição')),
                ('tempo_de_duracao', models.TimeField(blank=True, null=True, verbose_name='Tempo de duração')),
                ('preco', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Preço')),
            ],
            options={
                'verbose_name': 'Serviço',
                'verbose_name_plural': 'Serviços',
            },
        ),
    ]

# Generated by Django 4.0.1 on 2024-08-31 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0020_remove_servico_tempo_de_duracao'),
    ]

    operations = [
        migrations.AddField(
            model_name='servico',
            name='tempo_de_duracao_minutos',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Tempo de Duração (em minutos)'),
        ),
    ]

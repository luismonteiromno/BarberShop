# Generated by Django 4.0.1 on 2024-06-13 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0014_servico_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='meuagendamento',
            name='cancelar_agendamento',
            field=models.BooleanField(default=False, verbose_name='Deseja cancelar este agendamento?'),
        ),
    ]
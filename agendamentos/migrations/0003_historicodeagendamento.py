# Generated by Django 4.0.1 on 2024-05-06 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agendamentos', '0002_agendamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricoDeAgendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_do_agendamento', models.DateTimeField(blank=True, null=True, verbose_name='Data do agendamento')),
                ('barbeiro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='barbeiro_agendado', to=settings.AUTH_USER_MODEL, verbose_name='Barbeiro')),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Cliente')),
                ('servico_fornecido', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='agendamentos.servico', verbose_name='Serviço fornecido')),
            ],
            options={
                'verbose_name': 'Histórico de agendamento',
                'verbose_name_plural': 'Histórico de agendamentos',
            },
        ),
    ]

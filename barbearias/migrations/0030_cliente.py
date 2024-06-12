# Generated by Django 4.0.1 on 2024-06-08 21:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('barbearias', '0029_planosdefidelidade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Cliente')),
                ('plano_de_fidelidade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='barbearias.planosdefidelidade', verbose_name='Plano de fidelidade')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]
# Generated by Django 4.0.1 on 2024-06-03 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barbearias', '0025_barbeiro_salario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='financeiro',
            name='renda_semanal',
        ),
    ]

# Generated by Django 4.0.1 on 2024-06-29 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barbearias', '0051_funcionario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='data_de_admissao',
        ),
    ]
# Generated by Django 4.0.1 on 2024-05-06 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barbearias', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barbearia',
            name='servicos',
        ),
    ]

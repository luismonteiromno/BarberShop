# Generated by Django 4.0.1 on 2024-07-13 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barbearias', '0058_remove_barbeiro_barbearia_barbeiro_barbearias'),
    ]

    operations = [
        migrations.AddField(
            model_name='barbearia',
            name='barbeiros',
            field=models.ManyToManyField(to='barbearias.Barbeiro', verbose_name='Barbeiros'),
        ),
    ]
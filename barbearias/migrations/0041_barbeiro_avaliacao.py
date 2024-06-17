# Generated by Django 4.0.1 on 2024-06-16 22:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barbearias', '0040_planosdefidelidade_cor_do_cartao'),
    ]

    operations = [
        migrations.AddField(
            model_name='barbeiro',
            name='avaliacao',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Avaliação do barbeiro'),
        ),
    ]

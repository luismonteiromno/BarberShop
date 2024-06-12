# Generated by Django 4.0.1 on 2024-06-01 18:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barbearias', '0019_contato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='avaliacao',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Avaliação'),
        ),
    ]
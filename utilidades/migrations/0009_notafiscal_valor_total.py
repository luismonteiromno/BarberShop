# Generated by Django 4.0.1 on 2024-08-11 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilidades', '0008_notafiscal_compra'),
    ]

    operations = [
        migrations.AddField(
            model_name='notafiscal',
            name='valor_total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Valor total'),
        ),
    ]

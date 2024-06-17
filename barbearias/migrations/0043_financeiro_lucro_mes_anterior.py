# Generated by Django 4.0.1 on 2024-06-17 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barbearias', '0042_avaliacaodobarbeiro'),
    ]

    operations = [
        migrations.AddField(
            model_name='financeiro',
            name='lucro_mes_anterior',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True, verbose_name='Lucro do mês anterior'),
        ),
    ]
# Generated by Django 4.0.1 on 2024-08-31 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utilidades', '0023_produto_lucro_atraves_desse_produto'),
    ]

    operations = [
        migrations.AddField(
            model_name='promocao',
            name='produto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='utilidades.produto', verbose_name='Produto'),
        ),
    ]
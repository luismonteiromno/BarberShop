# Generated by Django 4.0.1 on 2024-06-13 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0013_categoriadoservico'),
    ]

    operations = [
        migrations.AddField(
            model_name='servico',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='agendamentos.categoriadoservico', verbose_name='Categoria'),
        ),
    ]

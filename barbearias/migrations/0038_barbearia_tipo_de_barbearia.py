# Generated by Django 4.0.1 on 2024-06-10 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barbearias', '0037_barbearia_horario_de_abertura_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='barbearia',
            name='tipo_de_barbearia',
            field=models.CharField(blank=True, choices=[('Própria', 'Própria'), ('Parceira', 'Parceira'), ('Locação', 'Locação')], max_length=100, null=True, verbose_name='Tipo de barbearia'),
        ),
    ]
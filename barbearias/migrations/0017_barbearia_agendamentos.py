# Generated by Django 4.0.1 on 2024-05-16 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barbearias', '0016_remove_barbearia_agendamentos'),
    ]

    operations = [
        migrations.AddField(
            model_name='barbearia',
            name='agendamentos',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Agendamentos'),
        ),
    ]

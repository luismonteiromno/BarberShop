# Generated by Django 4.0.1 on 2024-05-16 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barbearias', '0015_alter_barbearia_agendamentos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barbearia',
            name='agendamentos',
        ),
    ]

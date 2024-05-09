# Generated by Django 4.0.1 on 2024-05-08 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_alter_profile_tipo_do_usuario'),
        ('barbearias', '0008_barbeiro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barbeiro',
            name='barbeiro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='barbeiro', to='usuarios.profile', verbose_name='Barbeiro'),
        ),
    ]

# Generated by Django 4.0.1 on 2024-06-29 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_cargo', models.CharField(max_length=100, verbose_name='Nome do Cargo')),
                ('nivel_hierarquico', models.CharField(choices=[('Gerente', 'Gerente'), ('Diretor', 'Diretor'), ('Supervisor', 'Supervisor'), ('Colaborador', 'Colaborador')], max_length=100, verbose_name='Nível hierárquico')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
        ),
    ]

# Generated by Django 4.0.1 on 2024-07-06 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barbearias', '0055_alter_funcionario_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barbearia',
            name='funcionarios',
            field=models.ManyToManyField(blank=True, related_name='funcionario', to='barbearias.Funcionario', verbose_name='Funcionários'),
        ),
    ]
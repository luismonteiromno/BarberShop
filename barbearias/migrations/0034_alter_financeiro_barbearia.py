# Generated by Django 4.0.1 on 2024-06-09 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('barbearias', '0033_alter_financeiro_barbearia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financeiro',
            name='barbearia',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='barbearias.barbearia', verbose_name='Barbearia'),
        ),
    ]

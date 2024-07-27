# Generated by Django 4.0.1 on 2024-07-26 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('barbearias', '0070_alter_planosdefidelidade_barbearia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chavepix',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='barbearias.cliente', verbose_name='Cliente'),
        ),
    ]

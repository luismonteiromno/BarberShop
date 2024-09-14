# Generated by Django 4.0.1 on 2024-09-14 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilidades', '0025_remove_produto_tipo_do_produto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='status',
            field=models.CharField(blank=True, choices=[('Em andamento', 'Em andamento'), ('Cancelada', 'Cancelada'), ('Enviada', 'Enviada'), ('A caminho', 'A caminho'), ('Entregue', 'Entregue')], default='Em andamento', max_length=20, null=True, verbose_name='Status'),
        ),
    ]
# Generated by Django 4.0.1 on 2024-08-23 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('barbearias', '0075_remove_planosdefidelidade_quantidade_de_cortes'),
        ('utilidades', '0016_notafiscal_valor_unitario'),
    ]

    operations = [
        migrations.AddField(
            model_name='notafiscal',
            name='barbearia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='barbearias.barbearia', verbose_name='Barbearia'),
        ),
        migrations.AddField(
            model_name='notafiscal',
            name='status',
            field=models.CharField(blank=True, choices=[('Pendente', 'Pendente'), ('Em andamento', 'Em andamento'), ('Cancelada', 'Cancelada'), ('Preparando envio', 'Preparando envio'), ('Enviada', 'Enviada'), ('A caminho', 'A caminho'), ('Entregue', 'Entregue')], default='Pendente', max_length=20, null=True, verbose_name='Status'),
        ),
    ]

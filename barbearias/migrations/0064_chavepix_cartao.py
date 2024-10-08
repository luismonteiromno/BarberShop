# Generated by Django 4.0.1 on 2024-07-14 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('barbearias', '0063_metododepagamento_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChavePix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pix', models.CharField(max_length=200, unique=True, verbose_name='Chave PIX')),
                ('data_de_criacao', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data de criação')),
                ('data_de_atualizacao', models.DateTimeField(auto_now=True, null=True, verbose_name='Data de atualização')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barbearias.cliente', verbose_name='Cliente')),
            ],
            options={
                'verbose_name': 'Chave PIX',
                'verbose_name_plural': 'Chaves PIX',
            },
        ),
        migrations.CreateModel(
            name='Cartao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(blank=True, max_length=100, null=True, verbose_name='Número do cartão')),
                ('cvv', models.CharField(max_length=3, verbose_name='CVV')),
                ('tipo_do_cartao', models.CharField(blank=True, choices=[('Crédito', 'Crédito'), ('Débito', 'Débito')], max_length=10, null=True, verbose_name='Tipo do cartão')),
                ('validade', models.DateField(blank=True, null=True, verbose_name='Validade do cartão')),
                ('data_de_criacao', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data de criação')),
                ('data_de_atualizacao', models.DateTimeField(auto_now=True, null=True, verbose_name='Data de atualização')),
                ('titular', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barbearias.cliente', verbose_name='Titular do cartão')),
            ],
            options={
                'verbose_name': 'Cartão',
                'verbose_name_plural': 'Cartões',
            },
        ),
    ]

# Generated by Django 4.0.1 on 2024-05-07 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('barbearias', '0007_alter_barbearia_cnpj'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aviso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.ImageField(blank=True, null=True, upload_to='banners', verbose_name='Banner')),
                ('data_de_inicio', models.DateTimeField(blank=True, null=True, verbose_name='Data de início')),
                ('data_de_encerramento', models.DateTimeField(blank=True, null=True, verbose_name='Data de encerramento')),
                ('barbearia', models.ForeignKey(blank=True, help_text='Obs: Este só precisa ser preenchido caso o aviso afete alguma barbearia!', null=True, on_delete=django.db.models.deletion.SET_NULL, to='barbearias.barbearia', verbose_name='Barbearia')),
            ],
        ),
    ]

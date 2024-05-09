from django.db import models
from barbearias.models import Barbearia

class Aviso(models.Model):
    barbearia = models.ForeignKey(
        Barbearia,
        verbose_name='Barbearia',
        help_text='Obs: Este só precisa ser preenchido caso o aviso afete alguma barbearia!',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    
    banner = models.ImageField(
        verbose_name='Banner',
        upload_to='banners',
        blank=True,
        null=True,
    )
    
    data_de_inicio = models.DateTimeField(
        'Data de início',
        blank=True,
        null=True
    )
    
    data_de_encerramento = models.DateTimeField(
        'Data de encerramento',
        blank=True,
        null=True
    )

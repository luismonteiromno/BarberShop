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
    
    data_de_inicio = models.DateField(
        'Data de início',
        blank=True,
        null=True
    )
    
    data_de_encerramento = models.DateField(
        'Data de encerramento',
        blank=True,
        null=True
    )
    
    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = 'Aviso'
        verbose_name_plural = 'Avisos'
        
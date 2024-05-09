from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .barbearia import Barbearia
from django.contrib.auth.models import User

class Avaliacao(models.Model):
    avaliacao = models.FloatField(
        'Avaliação',
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        blank=True,
        null=True
    )
    
    barbearia = models.ForeignKey(
        Barbearia,
        verbose_name='Barbearia',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    
    usuario = models.ForeignKey(
        User,
        verbose_name='Usuário',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    
    def __str__(self):
        return str(self.avaliacao)
    
    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
    
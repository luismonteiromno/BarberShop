from django.core.validators import (
    MaxValueValidator,
    MinValueValidator
)
from django.db import models

from .barbeiro import Barbeiro

class AvaliacaoDoBarbeiro(models.Model):
    barbeiro = models.ForeignKey(
        Barbeiro,
        verbose_name='Barbeiro',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='barbeiro_avaliacao'
    )
    
    avaliacao = models.DecimalField(
        'Avaliação do barbeiro',
        max_digits=5,
        decimal_places=1,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        blank=True,
        null=True,
    )
    
    
    def __str__(self):
        return f'{str(self.barbeiro)} - {str(self.avaliacao)}'
    
    class Meta:
        verbose_name = 'Avaliação do barbeiro'
        verbose_name_plural = 'Avaliações do barbeiro'
from crum import get_current_user
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .barbearia import Barbearia


class Avaliacao(models.Model):
    avaliacao = models.DecimalField(
        'Avaliação',
        max_digits=5,
        decimal_places=1,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        blank=True,
        null=True
    )
    
    comentario = models.TextField(
        'Comentário',
        max_length=500,
        blank=True,
        null=True,
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
    
    def save(self, *args, **kwargs):
        user = get_current_user()
        if not self.pk:
            self.usuario = user  
        super().save(*args, **kwargs)
    
    def __str__(self):
        return str(self.avaliacao)
    
    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
    
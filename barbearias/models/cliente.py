from django.db import models
from django.contrib.auth.models import User

from .plano_fidelidade import PlanosDeFidelidade

class Cliente(models.Model):
    cliente = models.ForeignKey(
        User,
        verbose_name='Cliente',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    
    plano_de_fidelidade = models.ForeignKey(
        PlanosDeFidelidade,
        verbose_name='Plano de fidelidade',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    
    def __str__(self):
        return self.cliente.email
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
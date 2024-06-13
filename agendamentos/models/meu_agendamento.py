from django.db import models
from django.contrib.auth.models import User

from .agendamento import Agendamento

class MeuAgendamento(models.Model):
    agendamento = models.ForeignKey(
        Agendamento,
        verbose_name='Agendamento',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    
    cliente = models.ForeignKey(
        User,
        verbose_name='Cliente',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    
    def __str__(self):
        return f"{self.cliente} - {self.agendamento}"
    
    class Meta:
        verbose_name = 'Meu agendamento'
        verbose_name_plural = 'Meus agendamentos'
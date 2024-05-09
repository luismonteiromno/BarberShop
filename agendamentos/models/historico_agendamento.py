from django.db import models
from django.contrib.auth.models import User
from .servico import Servico

class HistoricoDeAgendamento(models.Model):
    servico_fornecido = models.ForeignKey(
        Servico, 
        verbose_name='Serviço fornecido',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    
    cliente = models.ForeignKey(
        User, 
        verbose_name='Cliente',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    
    barbeiro = models.ForeignKey(
        User, 
        verbose_name='Barbeiro',
        related_name='barbeiro_agendado',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    
    data_do_agendamento = models.DateTimeField(
        'Data do agendamento',
        blank=True,
        null=True
    )
    
    def __str__(self):
        return str(self.servico_fornecido)
    
    class Meta:
        verbose_name = 'Histórico de agendamento'
        verbose_name_plural = 'Histórico de agendamentos'
    
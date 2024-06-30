from django.contrib.auth.models import User
from django.db import models

from .agendamento import Agendamento
from barbearias.models import Cliente

class MeuAgendamento(models.Model):
    agendamento = models.ForeignKey(
        Agendamento,
        verbose_name='Agendamento',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    
    cliente = models.ForeignKey(
        Cliente,
        verbose_name='Cliente',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    
    cancelar_agendamento = models.BooleanField(
        'Deseja cancelar este agendamento?',
        default=False
    )
    
    @property
    def servico(self):
        return self.agendamento.servico if self.agendamento else None
    
    def cancelar_o_agendamento(self, obj):
        obj.cancelar_agendamento = True
        obj.agendamento.agendamento_cancelado = True
        # salvar o status direto no agendamento
        obj.agendamento.save()
        # salvar o status direto no meu agendamento
        obj.save()
        
    def __str__(self):
        return f"{self.cliente} - {self.agendamento}"
    
    class Meta:
        verbose_name = 'Meu agendamento'
        verbose_name_plural = 'Meus agendamentos'
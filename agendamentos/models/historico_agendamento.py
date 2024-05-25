from django.contrib.auth.models import User
from django.db import models

from .servico import Servico


class HistoricoDeAgendamento(models.Model):
    servico_fornecido = models.ForeignKey(
        Servico, 
        verbose_name='Serviço fornecido',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    
    preco_do_servico = models.DecimalField(
        'Preço do serviço',
        max_digits=10,
        decimal_places=2,
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
    
    @property
    def preco_total(self):
        preco = self.servico_fornecido.preco
        return preco if preco else 0
    
    @property
    def barbearia(self):
        barbearia = self.servico_fornecido.disponivel_na_barbearia
        return barbearia
    
    def save(self, *args, **kwargs):
        self.preco_do_servico = self.preco_total
        super().save(*args, **kwargs)
    
    def __str__(self):
        return str(self.servico_fornecido)
    
    class Meta:
        verbose_name = 'Histórico de agendamento'
        verbose_name_plural = 'Histórico de agendamentos'
    
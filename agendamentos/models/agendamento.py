from datetime import datetime
from decimal import Decimal

from crum import get_current_user
from django.contrib.auth.models import User
from django.db import models

from .servico import Servico


class Agendamento(models.Model):
    servico = models.ForeignKey(
        Servico,
        verbose_name='Serviço',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    
    escolher_barbeiro = models.ForeignKey(
        User,
        verbose_name='Escolher barbeiro',
        related_name='barbeiro_escolhido',
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
    
    preco_do_servico = models.DecimalField(
        'Preço do serviço',
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    
    data_marcada = models.DateTimeField(
        'Data marcada',
        blank=True,
        null=True
    )
    
    numero_do_agendamento = models.CharField(
        'Número do agendamento',
        max_length=100,
        blank=True,
        null=True,
        unique=True
    )
    
    @property
    def formatar_numero_do_pedido(self):
        ano = datetime.today().year
        mes = datetime.today().month
        agendamento_id = 0
        
        ultimo_agendamento = Agendamento.objects.last()
        
        if ultimo_agendamento:
            agendamento_id = int(ultimo_agendamento.numero_do_agendamento[12:]) + 1
        if not ultimo_agendamento or agendamento_id == 0:
            agendamento_id += 1
            
        if agendamento_id < 10:
            agendamento_id = f'0{agendamento_id}'
        if mes < 10:
            mes = f'0{mes}'
            
        numero_agendamento = f'BBSHP{ano}{mes}{agendamento_id}'
        return numero_agendamento        
    
    @property
    def preco_total(self):
        if self.pk:
            return Decimal(self.servico.preco)
        else:
            return Decimal(self.servico.preco)

    def save(self, *args, **kwargs):
        if not self.pk:
            user = get_current_user()
            self.usuario = user
            self.numero_do_agendamento = self.formatar_numero_do_pedido
            self.preco_do_servico = self.preco_total
        else:
            self.preco_do_servico = self.preco_total
        super().save(*args, **kwargs)
    
    def __str__(self):
        data_formatada = datetime.strftime(self.data_marcada, '%d/%m/%Y às %H:%M:%S')
        return f"{self.usuario} - {data_formatada}"
    
    class Meta:
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'

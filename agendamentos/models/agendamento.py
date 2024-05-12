from django.db import models
from .servico import Servico
from django.contrib.auth.models import User
from crum import get_current_user

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
    
    @property
    def preco_total(self):
        preco = self.servico.preco
        return preco if preco else 0

    def save(self, *args, **kwargs):
        if not self.pk:
            user = get_current_user()
            self.usuario = user
        self.preco_do_servico = self.preco_total
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.usuario} - {self.data_marcada}"
    
    class Meta:
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'

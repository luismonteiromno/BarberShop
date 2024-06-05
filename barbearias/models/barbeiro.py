from django.contrib.auth.models import User
from django.db import models

from .barbearia import Barbearia


class Barbeiro(models.Model):
    barbeiro = models.ForeignKey(
        User,
        verbose_name='Barbeiro',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='barbeiro'
    )
    
    servicos = models.ManyToManyField(
        'agendamentos.Servico',
        verbose_name='Serviços',
        blank=True,
    )
    
    barbearia = models.ForeignKey(
        Barbearia,
        verbose_name='Barbearia',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    
    salario = models.DecimalField(
        'Salário',
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )
    
    freelancer =  models.BooleanField(
        'Barbeiro Freelancer',
        default=False
    )
    
    def __str__(self):
        return str(self.barbeiro)
    
    class Meta:
        verbose_name = 'Barbeiro'
        verbose_name_plural = 'Barbeiros'
        
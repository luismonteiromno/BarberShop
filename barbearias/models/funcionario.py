from django.db import models
from cargos.models import Cargo

from ..models import Barbearia

class Funcionario(models.Model):
    barbearia = models.ForeignKey(
        Barbearia,
        verbose_name='Barbearia',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    
    nome = models.CharField(
        'Nome',
        max_length=100,
        blank=True,
        null=True,
    )
    
    cpf = models.CharField(
        'CPF',
        max_length=14,
    )
    
    cargo = models.ForeignKey(
        Cargo,
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
    
    def __str__(self):
        return self.nome or self.cpf
    
    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
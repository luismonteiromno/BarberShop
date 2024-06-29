from django.db import models
from cargos.models import Cargo


class Funcionario(models.Model):
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
    
    def __str__(self):
        return self.nome or self.cpf
    
    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
from django.db import models
from django.contrib.auth.models import User

from crum import get_current_user

class Barbearia(models.Model):
    dono = models.ForeignKey(
        User,
        verbose_name='Dono',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='barbearias'
    )
    
    nome_da_barbearia = models.CharField(
        'Nome da barbearia',
        max_length=100,
        blank=True,
        null=True
    )
    
    cnpj = models.CharField(
        'CNPJ',
        max_length=19,
        blank=True,
        null=True
    )
    
    funcionarios = models.ManyToManyField(
        User,
        verbose_name='Funcionários',
        blank=True
    )
    
    rua = models.CharField(
        'Rua',
        max_length=100,
        blank=True,
        null=True
    )
    
    bairro = models.CharField(
        'Bairro',
        max_length=100,
        blank=True,
        null=True
    )
    
    complemento = models.CharField(
        'Complemento',
        max_length=100,
        blank=True,
        null=True
    )
    
    cidade = models.CharField(
        'Cidade',
        max_length=100,
        blank=True,
        null=True
    )
    
    estado = models.CharField(
        'Estado',
        max_length=100,
        blank=True,
        null=True
    )
    
    cep = models.CharField(
        'CEP',
        max_length=16,
        blank=True,
        null=True
    )
    
    def save(self, *args, **kwargs):
        user = get_current_user()
        if not self.pk:
            self.dono = user      
        super().save()
        
    def __str__(self):
        return self.nome_da_barbearia
    
    class Meta:
        verbose_name = 'Barbearia'
        verbose_name_plural = 'Barbearias'
    
    
from colorfield.fields import ColorField
from django.db import models
from tinymce.models import HTMLField

from .barbearia import Barbearia
from .metodo_de_pagamento import MetodoDePagamento


class PlanosDeFidelidade(models.Model):
    barbearia = models.ForeignKey(
        Barbearia,
        verbose_name='Barbearia',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    
    nome = models.CharField(
        'Nome',
        max_length=100,
        blank=True,
        null=True,
    )
    
    cor_do_cartao = ColorField(
        'Cor do cartão',
        default='#808080',
        format='hexa',
        blank=True,
        null=True,
    )
    
    beneficios = HTMLField(
        'Beneficios',
        blank=True,
        null=True,
    )
    
    preco = models.DecimalField(
        'Mensalidade',
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )
    
    metodo_de_pagamento = models.ManyToManyField(
        MetodoDePagamento,
        verbose_name='Métodos de pagamento aceitáveis',
        blank=True
    )
    
    quantidade_de_cortes = models.PositiveIntegerField(
        'Quantidade de cortes',
        blank=True,
        null=True,
    )
    
    usuarios = models.PositiveIntegerField(
        'Quantidade de usuários que possuem esse plano',
        blank=True,
        null=True,
    )
    
    @property
    def quantidade_de_usuarios(self):
        usuarios = self.cliente_set.all().count()
        return usuarios
    
    def save(self, *args, **kwargs):
        self.usuarios = self.quantidade_de_usuarios
        super().save(*args, **kwargs)
    
    def __str__(self):
        return str(self.nome)
    
    class Meta:
        verbose_name = 'Plano de fidelidade'
        verbose_name_plural = 'Planos de fidelidade'
    
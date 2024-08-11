from django.db import models

from barbearias.models import Cliente
from .produto import Produto

class Compra(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        verbose_name='Cliente',
        on_delete=models.PROTECT,
    )
    
    produto = models.ForeignKey(
        Produto,
        verbose_name='Produto',
        on_delete=models.PROTECT,
    )
    
    quantidade = models.PositiveIntegerField(
        'Quantidade',
        help_text='Quantidade de unidades do produto',
    )

    preco_total = models.DecimalField(
        'Preço total',
        max_digits=10,
        decimal_places=2,
    )
    
    data_da_compra = models.DateField(
        'Data da compra',
        auto_now_add=True
    )
    
    @property
    def calcular_preco_total(self):
        return self.produto.preco * self.quantidade
    
    def save(self, *args, **kwargs):
        self.preco_total = self.calcular_preco_total
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.produto.nome} - {self.quantidade} unidades'

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'

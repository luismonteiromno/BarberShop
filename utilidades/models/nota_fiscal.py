from django.db import models
from barbearias.models import Cliente
from .produto import Produto

class NotaFiscal(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        verbose_name='Cliente',
        on_delete=models.PROTECT,
    )
    
    numero = models.CharField(
        'Número',
        max_length=100,
    )
    
    produto = models.ForeignKey(
        Produto,
        verbose_name='Produto',
        on_delete=models.PROTECT,
    )
    
    quantidade_comprada = models.PositiveIntegerField(
        'Quantidade comprada',
        default=0
    )
    
    valor_unitario = models.DecimalField(
        'Valor unitário',
        max_digits=10,
        decimal_places=2,
        default=0.00
    )
    
    valor_total = models.DecimalField(
        'Valor total',
        max_digits=10,
        decimal_places=2,
        default=0.0
    )
    
    data_emissao = models.DateField(
        'Data de emissão',
    )
    
    def __str__(self):
        return f'{self.numero} - {self.cliente}'
    
    class Meta:
        verbose_name = 'Nota Fiscal'
        verbose_name_plural = 'Notas Fiscais'
    
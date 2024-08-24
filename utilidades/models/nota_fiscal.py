from django.db import models
from barbearias.models import Barbearia, Cliente

from .produto import Produto

class NotaFiscal(models.Model): 
    barbearia = models.ForeignKey(
        Barbearia,
        verbose_name='Barbearia',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    
    cliente = models.ForeignKey(
        Cliente,
        verbose_name='Cliente',
        on_delete=models.PROTECT,
    )
    
    compra = models.ForeignKey(
        'Compra',
        verbose_name='Compra',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='notafiscal_compra'
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
    
    STATUS = (
        ('Pendente', 'Pendente'),
        ('Em andamento', 'Em andamento'),
        ('Cancelada', 'Cancelada'),
        ('Preparando envio', 'Preparando envio'),
        ('Enviada', 'Enviada'),
        ('A caminho', 'A caminho'),
        ('Entregue', 'Entregue'),
    )
    
    status = models.CharField(
        'Status',
        max_length=20,
        choices=STATUS,
        default='Pendente',
        blank=True,
        null=True,
    )
    
    data_emissao = models.DateField(
        'Data de emissão',
    )
    
    def __str__(self):
        return f'{self.numero} - {self.cliente}'
    
    class Meta:
        verbose_name = 'Nota Fiscal'
        verbose_name_plural = 'Notas Fiscais'
    
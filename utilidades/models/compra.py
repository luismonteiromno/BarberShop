from django.db import models
from crum import get_current_user

from barbearias.models import Cliente
from .nota_fiscal import NotaFiscal
from .produto import Produto

class Compra(models.Model):
    
    cliente = models.ForeignKey(
        Cliente,
        verbose_name='Cliente',
        on_delete=models.PROTECT,
    )
    
    nota_fiscal = models.ForeignKey(
        NotaFiscal,
        verbose_name='Nota Fiscal',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='compra_notafiscal'
    )
    
    produto = models.ForeignKey(
        Produto,
        verbose_name='Produto',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    
    quantidade = models.PositiveIntegerField(
        'Quantidade',
        help_text='Quantidade de unidades do produto',
    )
    
    preco_unitario = models.DecimalField(
        'Preço unitário',
        max_digits=10,
        decimal_places=2,
        default=0.00
    )

    preco_total = models.DecimalField(
        'Preço total',
        max_digits=10,
        decimal_places=2,
    )
    
    STATUS = (
        ('Em andamento', 'Em andamento'),
        ('Cancelada', 'Cancelada'),
        ('Enviada', 'Enviada'),
        ('A caminho', 'A caminho'),
        ('Entregue', 'Entregue'),
    )
    
    status = models.CharField(
        'Status',
        max_length=20,
        choices=STATUS,
        default='Em andamento',
        blank=True,
        null=True,
    )
    
    data_da_compra = models.DateField(
        'Data da compra',
        auto_now_add=True
    )
    
    @property
    def calcular_preco_total(self):
        return self.produto.preco * self.quantidade
    
    def save(self, *args, **kwargs):
        user = get_current_user()
        if not self.pk:
            self.cliente = Cliente.objects.get(cliente=user)
            self.preco_unitario = self.produto.preco
    
        self.preco_unitario = self.produto.preco
        self.preco_total = self.calcular_preco_total
        
        if self.produto and self.quantidade < 1:
            raise ValueError('Quantidade inválida')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.produto.nome} - {self.quantidade} unidades'

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'

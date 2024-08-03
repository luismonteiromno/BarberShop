from django.db import models
from tinymce.models import HTMLField

from agendamentos.models import CategoriaDoServico
from barbearias.models import Barbearia

class Produto(models.Model):
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
    )
    
    preco = models.DecimalField(
        'Preço',
        max_digits=10,
        decimal_places=2,
    )
    
    tipo_do_produto = models.ForeignKey(
        CategoriaDoServico,
        verbose_name='Tipo do produto',
        on_delete=models.PROTECT,
    )
    
    quantidade = models.PositiveIntegerField(
        'Quantidade',
        default=0,
    )
    
    ativo = models.BooleanField(
        'Ativo',
        default=True,
    )
    
    descricao = HTMLField(
        'Descrição/Instruções',
        blank=True,
        null=True,
    )
    
    data_de_criacao = models.DateTimeField(
        'Data de criação',
        auto_now_add=True,
        blank=True,
        null=True,
    )
    
    data_de_atualizacao = models.DateTimeField(
        'Data de atualização',
        auto_now=True,
        blank=True,
        null=True,
    )
    
    def __str__(self):
        return f'{self.nome}'
    
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        
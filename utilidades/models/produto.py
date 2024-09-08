from decimal import Decimal

from django.db import models
from django.db.models import Sum
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

    lucro_atraves_desse_produto = models.DecimalField(
        'Lucro através desse produto',
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
    )

    tipo_do_produto = models.ManyToManyField(
        CategoriaDoServico,
        verbose_name='Tipo do produto',
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

    quantidade_total_vendida = models.PositiveBigIntegerField(
        'Quantidade TOTAL vendida',
        default=0,
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

    @property
    def pegar_quantidade(self):
        quantidade = self.compra_set.aggregate(
            quantidade_total=Sum('quantidade')
        )['quantidade_total'] or Decimal('0.00')
        return quantidade

    @property
    def lucro_total(self):
        lucro = self.compra_set.aggregate(
            lucro=Sum('preco_total')
        )['lucro'] or Decimal('0.00')
        return lucro

    def save(self, *args, **kwargs):
        self.quantidade_total_vendida = self.pegar_quantidade
        self.lucro_atraves_desse_produto = self.lucro_total
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.nome}'

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

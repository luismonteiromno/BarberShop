from django.db import models
from .cliente import Cliente


class Cartao(models.Model):
    TIPO_DO_CARTAO = (
        ('Crédito', 'Crédito'),
        ('Débito', 'Débito')
    )
    titular = models.ForeignKey(
        Cliente,
        verbose_name='Titular do cartão',
        on_delete=models.CASCADE
    )
    
    numero = models.CharField(
        'Número do cartão',
        max_length=100,
        blank=True,
        null=True,
    )
    
    cvv = models.CharField(
        'CVV',
        max_length=3
    )
    
    tipo_do_cartao = models.CharField(
        'Tipo do cartão',
        max_length=10,
        choices=TIPO_DO_CARTAO,
        blank=True,
        null=True,
    )
    
    cartao_bloqueado = models.BooleanField(
        'Cartão bloqueado',
        default=False
    )
    
    validade = models.DateField(
        'Validade do cartão',
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
        return f'{self.titular}'
    
    class Meta:
        verbose_name = 'Cartão'
        verbose_name_plural = 'Cartões'

from django.db import models

from .cliente import Cliente

class ChavePix(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        verbose_name='Cliente',
        on_delete=models.CASCADE
    )
    
    pix = models.CharField(
        'Chave PIX',
        max_length=200,
        unique=True,
    )
    
    chave_aleatoria = models.BooleanField(
        'Chave aleatória',
        default=False,
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
        return f'{self.cliente.cliente.username}'
    
    class Meta:
        verbose_name = 'Chave PIX'
        verbose_name_plural = 'Chaves PIX'

from django.db import models


class Promocao(models.Model):
    servico = models.ForeignKey(
        'agendamentos.Servico',
        verbose_name='Serviço',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    
    produto = models.ForeignKey(
        'utilidades.Produto',
        verbose_name='Produto',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    
    plano_fidelidade = models.ForeignKey(
        'barbearias.PlanosDeFidelidade',
        verbose_name='Plano de fidelidade',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    
    nome_da_promocao = models.CharField(
        'Nome da promoção',
        max_length=100,
        blank=True,
        null=True,
    )
    
    inicio_da_promocao = models.DateField(
        'Início da promoção',
        blank=True,
        null=True,
    )
    
    fim_da_promocao = models.DateField(
        'Fim da promoção',
        blank=True,
        null=True,
    )
    
    def __str__(self):
        return self.nome_da_promocao
    
    class Meta:
        verbose_name = 'Promoção'
        verbose_name_plural = 'Promoções'

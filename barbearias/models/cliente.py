from django.contrib.auth.models import User
from django.db import models, transaction

import pendulum
import logging

logger = logging.getLogger(__name__)

from .plano_fidelidade import PlanosDeFidelidade

from random import random
from decimal import Decimal


class Cliente(models.Model):
    cliente = models.OneToOneField(
        User,
        verbose_name='Cliente',
        on_delete=models.SET_NULL,
        unique=True,
        blank=True,
        null=True,
    )

    plano_de_fidelidade = models.ForeignKey(
        PlanosDeFidelidade,
        verbose_name='Plano de fidelidade',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    credito = models.DecimalField(
        'Crédito que cliente possue',
        help_text='Pode ser utilizado para obter desconto nos serviços',
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )

    def atualizar_credito_cliente(self, cliente):
        try:
            user = Cliente.objects.get(pk=cliente.id)
        except:
            for user in cliente:
                user = Cliente.objects.get(pk=user.id)
        logger.info(f'Cliente {user}')
        logger.info(f'Crédito atual: {user.credito}')
        if int(user.credito) < 50:
            user.credito += Decimal(random())
            user.save()
            logger.info(f'Crédito atualizado para: {user.credito}')
        else:
            logger.info(f'Crédito máximo já atingido para o cliente {user}')
            user.credito = 50

    def gerar_chave_aleatoria(self, cliente):
        import secrets
        from .chave_pix import ChavePix

        with transaction.atomic():
            token_pix = secrets.token_hex(32)
            if (
                ChavePix.objects.filter(
                    cliente=cliente, chave_aleatoria=True
                ).count()
                == 1
            ):
                raise Exception('Muitas chaves PIX aleatórias já existem')
            else:
                ChavePix.objects.create(
                    cliente=cliente,
                    pix=f'pix-{token_pix}',
                    chave_aleatoria=True,
                    data_de_criacao=pendulum.now(),
                    data_de_atualizacao=pendulum.now(),
                )
                logger.info(
                    f'Chave PIX gerada para o cliente {cliente}: pix-{token_pix}'
                )
                return f'Chave PIX gerada para o cliente {cliente}: pix-{token_pix}'

    def __str__(self):
        return self.cliente.email or str(self.cliente)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

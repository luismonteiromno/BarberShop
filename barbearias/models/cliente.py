from django.contrib.auth.models import User
from django.db import models

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
        "Crédito que cliente possue",
        help_text="Pode ser utilizado para obter desconto nos serviços",
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
        if user.credito < 50:
            if user.credito:
                user.credito += Decimal(random())
            else:
                user.credito = Decimal(random())
        else:
            user.credito = 50
        user.save()

    def __str__(self):
        return self.cliente.email

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

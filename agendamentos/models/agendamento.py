from datetime import datetime
from decimal import Decimal

from crum import get_current_user
from django.contrib.auth.models import User
from django.db import models

from barbearias.models import Cliente

from .servico import Servico


class Agendamento(models.Model):
    servico = models.ForeignKey(
        Servico,
        verbose_name='Serviço',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    escolher_barbeiro = models.ForeignKey(
        User,
        verbose_name='Escolher barbeiro',
        related_name='barbeiro_escolhido',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    cliente = models.ForeignKey(
        Cliente,
        verbose_name='Usuário',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    preco_do_servico = models.DecimalField(
        'Preço do serviço',
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )

    desconto_do_usuario = models.DecimalField(
        'Desconto atráves do crédito do cliente',
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )

    data_marcada = models.DateTimeField('Data marcada', blank=True, null=True)

    numero_do_agendamento = models.CharField(
        'Número do agendamento',
        max_length=100,
        blank=True,
        null=True,
        unique=True,
    )

    agendamento_cancelado = models.BooleanField(
        'Agendamento cancelado',
        default=False,
    )

    @property
    def formatar_numero_do_pedido(self):
        ano = datetime.today().year
        mes = datetime.today().month
        agendamento_id = 0

        ultimo_agendamento = Agendamento.objects.filter(
            data_marcada__year=ano, data_marcada__month=mes
        ).last()

        if ultimo_agendamento:
            agendamento_id = (
                int(ultimo_agendamento.numero_do_agendamento[11:]) + 1
            )
        elif not ultimo_agendamento or agendamento_id == 0:
            agendamento_id += 1

        if agendamento_id < 10:
            agendamento_id = f'0{agendamento_id}'
        if mes < 10:
            mes = f'0{mes}'

        numero_agendamento = f'BBSHP{ano}{mes}{agendamento_id}'
        return numero_agendamento

    @property
    def preco_total(self):
        user = get_current_user()
        self.desconto_do_usuario = (
            user.cliente.credito if user.cliente.credito else 0
        )
        if self.desconto_do_usuario > 0:
            desconto = (self.desconto_do_usuario / 100) * self.servico.preco
            return self.servico.preco - desconto
        else:
            return Decimal(self.servico.preco)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if not self.pk:
            self.cliente, created = Cliente.objects.get_or_create(
                cliente=user,
                defaults={
                    'credito': Decimal('0.00'),
                    'plano_de_fidelidade': self.cliente.plano_de_fidelidade
                    if self.cliente
                    else None,
                },
            )
            if created:
                print(f'cliente {self.cliente} criado')

            self.numero_do_agendamento = self.formatar_numero_do_pedido
            if user.cliente.credito:
                self.desconto_do_usuario = user.cliente.credito / 100
            self.preco_do_servico = self.preco_total
        super().save(*args, **kwargs)

    def __str__(self):
        data_formatada = datetime.strftime(
            self.data_marcada, '%d/%m/%Y às %H:%M'
        )
        return f'{self.cliente} - {data_formatada}'

    class Meta:
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'

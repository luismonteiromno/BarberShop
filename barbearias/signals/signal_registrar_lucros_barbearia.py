from decimal import Decimal

import pendulum
from django.db import transaction
from django.db.models import DecimalField, F, Sum, Value
from django.db.models.functions import Coalesce
from django.db.models.signals import post_save
from django.dispatch import receiver

from agendamentos.models import Agendamento
from utilidades.models import Compra

from ..models import Barbearia, Barbeiro, Financeiro


@receiver(post_save, sender=Barbearia)
def registrar_lucros(sender, instance, created, **kwargs):
    if created:
        with transaction.atomic():
            Financeiro.objects.create(
                barbearia_id=instance.id,
                lucro_mes_anterior=0,
                renda_mensal=0,
                despesas=0,
                comparar_lucros_mes_anterior_e_atual_porcentagem=0,
                lucro_planos=0,
                lucro_total=0,
                receita_total=0,
                comparar_lucros_mes_anterior_e_atual=0,
                prejuizo=False,
                lucro=False,
            )
    else:
        mes_anterior = pendulum.now().date().subtract(months=1)
        
        barbearia = Barbearia.objects.get(pk=instance.id)
        barbeiros = Barbeiro.objects.prefetch_related('barbearias').filter(
            barbearias__in=[instance.id]
        )

        funcionarios = barbearia.funcionario_set.all()
        planos = barbearia.planosdefidelidade_set.all()

        produtos = Compra.objects.filter(
            produto__barbearia=barbearia
        ).aggregate(
            total=Coalesce(
                Sum('preco_total', output_field=DecimalField()),
                Value(Decimal('0.00')),
            )
        )[
            'total'
        ]

        agendamentos = Agendamento.objects.filter(
            data_marcada__lt=pendulum.now(),
            servico__disponivel_na_barbearia=barbearia,
            agendamento_cancelado=False,
        )
        lucro_anterior = agendamentos.filter(
            data_marcada__month=mes_anterior.month,
            data_marcada__year=mes_anterior.year,
        )
        lucro_mensal = agendamentos.filter(
            data_marcada__month=pendulum.now().month
        )

        calcular = Financeiro()
        despesa_barbeiro = calcular.salarios(barbeiros)
        despesa_funcionario = calcular.salarios(funcionarios)

        despesas = despesa_barbeiro + despesa_funcionario

        lucro_planos = (
            planos.filter(usuarios__gte=1)
            .annotate(lucro_planos=F('preco') * F('usuarios'))
            .aggregate(
                lucro_total=Coalesce(
                    Sum('lucro_planos', output_field=DecimalField()),
                    Value(Decimal('0.00')),
                ),
            )['lucro_total']
        ) or Decimal('0.00')

        receita = (
            calcular.lucros(agendamentos) + lucro_planos + produtos
        ) or Decimal('0.00')

        lucro_total = (
            calcular.lucros(agendamentos) + lucro_planos + produtos - despesas
        )
        lucro_mes = (
            calcular.lucros(lucro_mensal) + lucro_planos + produtos - despesas
        )
        lucro_mes_anterior = (
            calcular.lucros(lucro_anterior)
            + lucro_planos
            + produtos
            - despesas
        )

        comparar_lucros = Decimal(lucro_mes - lucro_mes_anterior)
        comparar_lucros_porcentagem = Decimal(comparar_lucros / 100).quantize(
            Decimal('0.00')
        )

        # como é porcentagem ent segue a seguinte regra
        # 1 = 100%
        # 0,9 = 90%
        # 0,8 = 80%
        # 0,7 = 70%
        # 0,6 = 60%
        # 0,5 = 50%
        # 0,4 = 40%
        # 0,3 = 30%
        # 0,2 = 20%
        # 0,1 = 10%
        # 0,0 = 0%

        print(
            f'Lucro do mês: {lucro_mes}',
            f'Lucro do mês anterior: {lucro_mes_anterior}',
            f'Despesas: {despesas}',
            f'comparar valores porcentagem: {comparar_lucros_porcentagem}',
            f'Lucro dos planos: {lucro_planos if lucro_planos else Decimal("0.00")}',
            f'Lucro total: {lucro_total}',
            f'lucro_produtos: {produtos}',
            f'Receita total: {receita}',
            f'Comparar lucros: {comparar_lucros}',
        )

        with transaction.atomic():
            Financeiro.objects.filter(barbearia=barbearia).update(
                lucro_mes_anterior=lucro_mes_anterior,
                renda_mensal=lucro_mes,
                despesas=despesas,
                comparar_lucros_mes_anterior_e_atual_porcentagem=comparar_lucros_porcentagem,
                lucro_planos=lucro_planos,
                lucro_total=lucro_total,
                lucro_produtos=produtos,
                receita_total=receita,
                comparar_lucros_mes_anterior_e_atual=comparar_lucros,
                prejuizo=comparar_lucros < 0,
                lucro=comparar_lucros > 0,
            )

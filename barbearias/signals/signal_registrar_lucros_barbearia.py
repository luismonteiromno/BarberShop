import pendulum
from decimal import Decimal
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from agendamentos.models import Agendamento, Servico

from ..models import Barbearia, Barbeiro, Financeiro


@receiver(post_save, sender=Barbearia)
def registrar_lucros(sender, instance, created, **kwargs):
    if created:
        Financeiro.objects.create(
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
        mes_anterior = pendulum.now().subtract(months=1)

        barbearia = Barbearia.objects.get(pk=instance.id)

        barbeiros = barbearia.barbeiro_set.all()
        funcionarios = barbearia.funcionario_set.all()
        planos = barbearia.planosdefidelidade_set.all()

        agendamentos = Agendamento.objects.filter(
            data_marcada__lt=pendulum.now(),
            servico__disponivel_na_barbearia=barbearia,
            agendamento_cancelado=False,
        )
        lucro_anterior = agendamentos.filter(
            data_marcada__month=mes_anterior.month, data_marcada__year=mes_anterior.year
        )
        lucro_mensal = agendamentos.filter(data_marcada__month=pendulum.now().month)

        despesa_barbeiro = Decimal(sum(barbeiro.salario for barbeiro in barbeiros))
        despesa_funcionario = Decimal(
            sum(funcionario.salario for funcionario in funcionarios)
        )
        despesas = despesa_barbeiro + despesa_funcionario

        # lucro_planos = Decimal(sum(lucro.preco*lucro.quantidade_de_usuarios for lucro in planos))
        lucro_planos = Decimal(0.00)
        for lucro in planos:
            lucro_planos = lucro.preco * lucro.quantidade_de_usuarios

        receita = Decimal(sum(lucro.preco_do_servico for lucro in agendamentos))
        lucro_total = (
            Decimal(sum(lucro.preco_do_servico for lucro in agendamentos))
            + lucro_planos
        ) - despesas

        lucro_mes = (
            Decimal(sum(lucro.preco_do_servico for lucro in lucro_mensal))
            + lucro_planos
        ) - despesas
        lucro_mes_anterior = (
            Decimal(sum(lucro.preco_do_servico for lucro in lucro_anterior))
            + lucro_planos
        ) - despesas
        receita = Decimal(sum(lucro.preco_do_servico for lucro in agendamentos))

        comparar_lucros = Decimal(lucro_mes - lucro_mes_anterior)
        comparar_lucros_porcentagem = Decimal(comparar_lucros / 100).quantize(
            Decimal("0.0")
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
            f"Lucro do mês: {lucro_mes}",
            f"Lucro do mês anterior: {lucro_mes_anterior}",
            f"Despesas: {despesas}",
            f"comparar valores porcentagem: {comparar_lucros_porcentagem}",
            f"Lucro dos planos: {lucro_planos}",
            f"Lucro total: {lucro_total}",
            f"Receita total: {receita}",
            f"Comparar lucros: {comparar_lucros}",
        )

        with transaction.atomic():
            Financeiro.objects.filter(barbearia=barbearia).update(
                lucro_mes_anterior=lucro_mes_anterior,
                renda_mensal=lucro_mes,
                despesas=despesas,
                comparar_lucros_mes_anterior_e_atual_porcentagem=comparar_lucros_porcentagem,
                lucro_planos=lucro_planos,
                lucro_total=lucro_total,
                receita_total=receita,
                comparar_lucros_mes_anterior_e_atual=comparar_lucros,
            )

from django_cron import Schedule, CronJobBase

from django.db import transaction
from ..models import Barbearia
from agendamentos.models import Agendamento
import pendulum
import logging

logger = logging.getLogger(__name__)


class AtualizarFinancasCronJob(CronJobBase):
    RUN_EVERY_MINS = 10  # every 10 minutes

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)

    code = "barbearias.atualizar_financas"

    def do(self):
        mes_anterior = pendulum.now().subtract(months=1)
        barbearias = Barbearia.objects.all()
        for barbearia in barbearias:
            instancia = Barbearia.objects.get(id=barbearia.id)
            barbeiros = barbearia.barbeiro_set.all()
            planos = barbearia.planosdefidelidade_set.all()
            financeiro = instancia.financeiro
            agendamentos = Agendamento.objects.filter(
                data_marcada__lt=pendulum.now(),
                servico__disponivel_na_barbearia=barbearia,
                agendamento_cancelado=False,
            )
            lucro_mensal_anterior = agendamentos.filter(
                data_marcada__month=mes_anterior.month,
                data_marcada__year=mes_anterior.year,
            )
            lucro_mensal = agendamentos.filter(data_marcada__month=pendulum.now().month)

            despesas = sum(barbeiro.salario for barbeiro in barbeiros)
            lucro_planos = sum(lucro.preco for lucro in planos)
            lucro_mes = sum(lucro.preco_do_servico for lucro in lucro_mensal)
            lucro_total = (
                sum(lucro.preco_do_servico for lucro in agendamentos) + lucro_planos
            ) - despesas
            lucro_mes_anterior = (
                sum(lucro.preco_do_servico for lucro in lucro_mensal_anterior)
                + lucro_planos
            ) - despesas
            receita = sum(lucro.preco_do_servico for lucro in agendamentos)

            comparar_lucros = lucro_mes - lucro_mes_anterior
            print(f"Comparar Lucros: {comparar_lucros}")
            print(f"Lucro Mes: {lucro_mes}")
            print(f"Lucro Mes anterior: {lucro_mes_anterior}")
            print(f"Despesas: {despesas}")
            print(f"Lucro Planos: {lucro_planos}")
            print(f"Lucro Total: {lucro_total}")
            print(f"Receita: {receita}")

            with transaction.atomic():
                financeiro.renda_mensal = lucro_mes
                financeiro.lucro_mes_anterior = lucro_mes_anterior
                financeiro.despesas = despesas
                financeiro.comparar_lucros_mes_anterior_e_atual = comparar_lucros
                financeiro.lucro_planos = lucro_planos
                financeiro.lucro_total = lucro_total
                financeiro.receita_total = receita
                financeiro.prejuizo = lucro_total < 0
                financeiro.lucro = lucro_total > 0
                financeiro.save()

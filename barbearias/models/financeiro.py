from decimal import Decimal

from django.db import models, transaction
from django.db.models import Q

from ..models import Barbearia


class Financeiro(models.Model):
    barbearia = models.OneToOneField(
        Barbearia,
        verbose_name="Barbearia",
        on_delete=models.SET_NULL,
        unique=True,
        blank=True,
        null=True,
    )

    lucro_mes_anterior = models.DecimalField(
        "Lucro do mês anterior", 
        max_digits=10, 
        decimal_places=5, 
        blank=True, 
        null=True
    )

    renda_mensal = models.DecimalField(
        "Renda mensal",
        help_text="Seu Lucro do mês",
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )

    despesas = models.DecimalField(
        "Despesas",
        help_text="Salários, produtos etc...",
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )

    comparar_lucros_mes_anterior_e_atual = models.DecimalField(
        "Lucro do mês atual em comparação ao anterior",
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )

    lucro_planos = models.DecimalField(
        "Lucro dos planos de fidelidade",
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )

    lucro_total = models.DecimalField(
        "Lucro total", 
        max_digits=10, 
        decimal_places=2, 
        blank=True, 
        null=True
    )

    receita_total = models.DecimalField(
        "Receita total", 
        max_digits=10, 
        decimal_places=2, 
        blank=True, 
        null=True
    )

    prejuizo = models.BooleanField(
        "Prejuízo", 
        default=False
    )

    lucro = models.BooleanField(
        "Lucro", 
        default=False
    )

    def atualizar_financas(self, financeiro):
        import pendulum

        from agendamentos.models import Agendamento

        mes_anterior = pendulum.now().subtract(months=1)
        try:
            # Caso o valor do parâmetro venha do Admin
            barbearia = Barbearia.objects.get(pk=financeiro.barbearia.id)
        except:
            # Caso o valor do parâmetro venha do Cron
            barbearia = Barbearia.objects.get(pk=financeiro.id)

        barbeiros = barbearia.barbeiro_set.all()
        planos = barbearia.planosdefidelidade_set.all()

        agendamentos = Agendamento.objects.filter(
            data_marcada__lt=pendulum.now(),
            servico__disponivel_na_barbearia=barbearia,
            agendamento_cancelado=False,
        )
        lucro_anterior = agendamentos.filter(
            data_marcada__month=mes_anterior.month, 
            data_marcada__year=mes_anterior.year
        )
        lucro_mensal = agendamentos.filter(data_marcada__month=pendulum.now().month)

        despesas = Decimal(sum(barbeiro.salario for barbeiro in barbeiros))
        lucro_planos = Decimal(sum(lucro.preco for lucro in planos))
        lucro_total = (
            Decimal(sum(lucro.preco_do_servico for lucro in agendamentos))
            + lucro_planos
        ) - despesas
        lucro_mes = (
            Decimal(sum(lucro.preco_do_servico for lucro in lucro_mensal))
            + lucro_planos
        )
        lucro_mes_anterior = (
            Decimal(sum(lucro.preco_do_servico for lucro in lucro_anterior))
            + lucro_planos
        ) - despesas
        receita = Decimal(sum(lucro.preco_do_servico for lucro in agendamentos))

        comparar_lucros = Decimal(lucro_mes - lucro_mes_anterior)
        
        print(
            f"Lucro do mês: {lucro_mes}",
            f"Lucro do mês anterior: {lucro_mes_anterior}" ,
            f"Despesas: {despesas}",
            f"Lucro dos planos: {lucro_planos}",
            f"Lucro total: {lucro_total}",
            f"Receita total: {receita}",
            f"Comparar lucros: {comparar_lucros}" 
        )

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

    # def atualizar_todas_as_financas(self, barbearias):
    #     import pendulum

    #     from agendamentos.models import Agendamento

    #     # mes_anterior = datetime.now() - relativedelta(months=1)
    #     mes_anterior = pendulum.now().subtract(months=1)
    #     for barbearia in barbearias:
    #         barbearia = Barbearia.objects.get(pk=barbearia.id)

    #         barbeiros = barbearia.barbeiro_set.all()
    #         planos = barbearia.planosdefidelidade_set.all()

    #         agendamentos = (
    #             Agendamento.objects.filter(
    #                 data_marcada__lt=pendulum.now(),
    #                 servico__disponivel_na_barbearia=barbearia,
    #                 agendamento_cancelado=False
    #             )
    #         )
    #         lucro_mes_anterior = agendamentos.filter(
    #             data_marcada__month=mes_anterior.month,
    #             data_marcada__year=mes_anterior.year
    #         )
    #         lucro_mensal = agendamentos.filter(
    #             data_marcada__month=pendulum.now().month
    #         )
    #         financeiros = barbearia.financeiro.__dict__

    #         despesas = Decimal(sum(barbeiro.salario for barbeiro in barbeiros))
    #         lucro_planos = Decimal(sum(lucro.preco for lucro in planos))
    #         lucro_total = (Decimal(sum(lucro.preco_do_servico for lucro in agendamentos)) + lucro_planos) - despesas
    #         lucro_mes = Decimal(sum(lucro.preco_do_servico for lucro in lucro_mensal)) + lucro_planos
    #         lucro_mes_anterior = (Decimal(sum(lucro.preco_do_servico for lucro in lucro_mes_anterior)) + lucro_planos) - despesas
    #         receita = Decimal(sum(lucro.preco_do_servico for lucro in agendamentos))

    #         comparar_lucros = Decimal(
    #             lucro_mes - lucro_mes_anterior
    #         )
    #         ...
    #         with transaction.atomic():
    #             for financeiro in list(financeiros):
    #                 financeiro.renda_mensal = lucro_mes
    #                 financeiro.lucro_mes_anterior = lucro_mes_anterior
    #                 financeiro.despesas = despesas
    #                 financeiro.comparar_lucros_mes_anterior_e_atual = comparar_lucros
    #                 financeiro.lucro_planos = lucro_planos
    #                 financeiro.lucro_total = lucro_total
    #                 financeiro.receita_total = receita
    #                 financeiro.prejuizo = lucro_total < 0
    #                 financeiro.lucro = lucro_total > 0
    #                 financeiro.save()

    def atualizar_todas_as_financas(self, financeiros):
        for financeiro in financeiros:
            try:
                # Caso o Parâmetro venha do Admin de Barbearias
                self.atualizar_financas(self, financeiro)
            except:
                # Caso o Parâmetro venha do Admin de Finanças
                Financeiro.atualizar_financas(self, financeiro)     
        
    def limpar_financeiro(self, fincanceiro):
        fincanceiro.renda_mensal = 0
        fincanceiro.despesas = 0
        fincanceiro.lucro_total = 0
        fincanceiro.lucro_planos = 0
        fincanceiro.receita_total = 0
        fincanceiro.prejuizo = False
        fincanceiro.lucro = False
        fincanceiro.save()

    def __str__(self):
        return self.barbearia.nome_da_barbearia

    class Meta:
        verbose_name = "Finança"
        verbose_name_plural = "Finanças"

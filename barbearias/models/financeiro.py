from decimal import Decimal

from django.db import models, transaction
from django.db.models import F, Q, Sum, Value
from django.db.models.functions import Coalesce

from ..models import Barbearia


class Financeiro(models.Model):
    barbearia = models.OneToOneField(
        Barbearia,
        verbose_name='Barbearia',
        on_delete=models.CASCADE,
        unique=True,
    )

    lucro_mes_anterior = models.DecimalField(
        'Lucro do mês anterior',
        max_digits=10,
        decimal_places=5,
        blank=True,
        null=True,
    )

    renda_mensal = models.DecimalField(
        'Renda mensal',
        help_text='Seu Lucro do mês',
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )

    despesas = models.DecimalField(
        'Despesas',
        help_text='Salários, produtos etc...',
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )

    comparar_lucros_mes_anterior_e_atual = models.DecimalField(
        'Lucro do mês atual em comparação ao anterior',
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )

    comparar_lucros_mes_anterior_e_atual_porcentagem = models.DecimalField(
        'Lucro do mês atual em comparação ao anterior(Porcentagem)',
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True,
    )

    lucro_planos = models.DecimalField(
        'Lucro dos planos de fidelidade',
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )

    lucro_total = models.DecimalField(
        'Lucro total', max_digits=10, decimal_places=2, blank=True, null=True
    )

    receita_total = models.DecimalField(
        'Receita total', max_digits=10, decimal_places=2, blank=True, null=True
    )

    prejuizo = models.BooleanField('Prejuízo', default=False)

    lucro = models.BooleanField('Lucro', default=False)

    def atualizar_financas(self, financeiro):
        import pendulum

        from agendamentos.models import Agendamento
        from .barbeiro import Barbeiro

        mes_anterior = pendulum.now().subtract(months=1)
        try:
            # Caso o valor do parâmetro venha do Admin
            barbearia = Barbearia.objects.get(pk=financeiro.barbearia.id)
            barbeiros = Barbeiro.objects.prefetch_related('barbearias').filter(
                barbearias__in=[financeiro.id]
            )
        except:
            # Caso o valor do parâmetro venha do Cron
            barbearia = Barbearia.objects.get(pk=financeiro.id)
            barbeiros = Barbeiro.objects.prefetch_related('barbearias').filter(
                barbearias__in=[financeiro.id]
            )

        funcionarios = barbearia.funcionario_set.all().select_related(
            'barbearia'
        )
        planos = barbearia.planosdefidelidade_set.all().select_related(
            'barbearia'
        )

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

        despesa_barbeiro = Decimal(
            barbeiros.aggregate(salario_total=Sum('salario'))['salario_total']
        ) if barbeiros else 0
        
        despesa_funcionario = Decimal(
            funcionarios.aggregate(salario_total=Sum('salario'))['salario_total']
        ) if funcionarios else 0
        
        despesas = despesa_barbeiro + despesa_funcionario

        lucro_planos = (planos.aggregate(
                preco=Sum(F('preco') * F('usuarios'))
        )) if planos else Decimal(0)

        receita = (
                agendamentos.aggregate(receita_total=Sum('preco_do_servico'))['receita_total']
        ) or Decimal(0)
        
        lucro_total = (
            agendamentos.aggregate(
                lucro_total=Sum('preco_do_servico')
            )['lucro_total']
        ) + lucro_planos - despesas if agendamentos else Decimal('0.00')

        lucro_mes = (
            lucro_mensal.aggregate(
                lucro_mes=Sum('preco_do_servico')
            )['lucro_mes']
        ) + lucro_planos - despesas if lucro_mensal else Decimal('0.00')
        
        lucro_mes_anterior = (
            lucro_anterior.aggregate(
                lucro_mes_anterior=Sum('preco_do_servico')
            )['lucro_mes_anterior']
        ) + lucro_planos - despesas if lucro_anterior else Decimal('0.00')

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
            f'Lucro dos planos: {lucro_planos}',
            f'Lucro total: {lucro_total}',
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
                receita_total=receita,
                comparar_lucros_mes_anterior_e_atual=comparar_lucros,
                prejuizo=comparar_lucros < 0,
                lucro=comparar_lucros > 0,
            )

    def atualizar_todas_as_financas(self, financeiros):
        for financeiro in financeiros:
            try:
                # Caso o Parâmetro venha do Admin de Barbearias
                self.atualizar_financas(financeiro)
            except:
                # Caso o Parâmetro venha do Admin de Finanças
                Financeiro().atualizar_financas(financeiro)

    def _limpar_financeiro(self, financeiro):
        financeiro.renda_mensal = 0
        financeiro.lucro_mes_anterior = 0
        financeiro.despesas = 0
        financeiro.comparar_lucros_mes_anterior_e_atual = 0
        financeiro.lucro_planos = 0
        financeiro.lucro_total = 0
        financeiro.receita_total = 0
        financeiro.prejuizo = False
        financeiro.lucro = False
        financeiro.save()

    def __str__(self):
        return self.barbearia.nome_da_barbearia

    class Meta:
        verbose_name = 'Finança'
        verbose_name_plural = 'Finanças'

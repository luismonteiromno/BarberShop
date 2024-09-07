from decimal import Decimal
from typing import Type

from django.db import models, transaction
from django.db.models import Count, F, Q, Sum, Value
from django.db.models.functions import Coalesce

from ..models import Barbearia


class Financeiro(models.Model):
    barbearia = models.OneToOneField(
        Barbearia,
        verbose_name='Barbearia',
        on_delete=models.SET_NULL,
        unique=True,
        null=True,
        blank=True
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

    lucro_produtos = models.DecimalField(
        'Lucro dos produtos',
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

    def lucros(self, model: Type[models.Model]) -> Decimal:
        lucro = model.aggregate(lucro=Sum('preco_do_servico'))['lucro'] or 0
        return Decimal(lucro)

    def salarios(self, model: Type[models.Model]) -> Decimal:
        salario_total = (
            model.aggregate(salario_total=Sum('salario'))['salario_total'] or 0
        )
        return Decimal(salario_total)

    def atualizar_financas(self, financeiro):
        import pendulum

        from agendamentos.models import Agendamento
        from utilidades.models import Compra

        from .barbeiro import Barbeiro

        mes_anterior = pendulum.now().date().subtract(months=1)
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

        funcionarios = barbearia.funcionario_set.all()
        planos = barbearia.planosdefidelidade_set.all()

        produtos = (
            Compra.objects.filter(produto__barbearia=barbearia).aggregate(
                lucro=Sum('preco_total')
            )['lucro'] or Decimal('0.00')
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

        # calcular = Financeiro()
        despesa_barbeiro = self.salarios(barbeiros)
        despesa_funcionario = self.salarios(funcionarios)

        despesas = despesa_barbeiro + despesa_funcionario

        lucro_planos = (
            (
                planos.filter(usuarios__gte=1)
                .values('preco')
                .annotate(lucro_planos=F('preco') * F('usuarios'))
                .aggregate(Sum('lucro_planos'))['lucro_planos__sum'] 
                or Decimal('0.00')
            )
        )

        receita = (
            self.lucros(agendamentos) + lucro_planos + produtos
        ) or Decimal('0.00')

        lucro_total = (
            self.lucros(agendamentos) + lucro_planos + produtos - despesas
        )
        lucro_mes = (
            self.lucros(lucro_mensal) + lucro_planos + produtos - despesas
        )
        lucro_mes_anterior = (
            self.lucros(lucro_anterior)
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
        financeiro.lucro_produtos = 0
        financeiro.receita_total = 0
        financeiro.prejuizo = False
        financeiro.lucro = False
        financeiro.save()

    def __str__(self):
        return self.barbearia.nome_da_barbearia

    class Meta:
        verbose_name = 'Finança'
        verbose_name_plural = 'Finanças'

from decimal import Decimal
from django.db import models, transaction
from django.db.models import Q

from ..models import Barbearia

class Financeiro(models.Model):
    barbearia = models.OneToOneField(
        Barbearia,
        verbose_name='Barbearia',
        on_delete=models.SET_NULL,
        unique=True,
        blank=True,
        null=True,
    )
    
    renda_mensal = models.DecimalField(
        'Renda mensal',
        help_text='Seu Lucro do mês',
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    
    despesas = models.DecimalField(
        'Despesas',
        help_text='Salários, produtos etc...',
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    
    lucro_planos = models.DecimalField(
        'Lucro dos planos de fidelidade',
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    
    lucro_total = models.DecimalField(
        'Lucro total',
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    
    receita_total = models.DecimalField(
        'Receita total',
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    
    prejuizo = models.BooleanField(
        'Prejuízo',
        default=False
    )
    
    lucro = models.BooleanField(
        'Lucro',
        default=False
    )
    
    def atualizar_financas(self, financeiro):
        from agendamentos.models import Agendamento
        import pendulum
        
        barbearia = Barbearia.objects.get(pk=financeiro.barbearia.id)
        barbeiros = barbearia.barbeiro_set.all()
        planos = barbearia.planosdefidelidade_set.all()
        
        agendamentos = (
            Agendamento.objects.filter(
                data_marcada__lt=pendulum.now(),
                servico__disponivel_na_barbearia=barbearia,
                agendamento_cancelado=False
            )
        )
        lucro_mensal = agendamentos.filter(
            data_marcada__month=pendulum.now().month 
        )
        
        despesas = Decimal(sum(barbeiro.salario for barbeiro in barbeiros))
        lucro_planos = Decimal(sum(lucro.preco for lucro in planos))
        lucro_total = (Decimal(sum(lucro.preco_do_servico for lucro in agendamentos)) + lucro_planos) - despesas
        lucro_mes = Decimal(sum(lucro.preco_do_servico for lucro in lucro_mensal)) + lucro_planos
        receita = Decimal(sum(lucro.preco_do_servico for lucro in agendamentos))
            
        with transaction.atomic(): 
            financeiro.renda_mensal = lucro_mes
            financeiro.despesas = despesas
            financeiro.lucro_planos = lucro_planos
            financeiro.lucro_total = lucro_total
            financeiro.receita_total = receita 
            financeiro.prejuizo = lucro_total < 0
            financeiro.lucro = lucro_total > 0
            financeiro.save()         
        
    def atualizar_todas_as_financas(self, barbearias):
        from agendamentos.models import Agendamento
        import pendulum
        
        for barbearia in barbearias:
            barbearia = Barbearia.objects.get(pk=barbearia.id)
            barbeiros = barbearia.barbeiro_set.all()
            planos = barbearia.planosdefidelidade_set.all()
            agendamentos = (
                Agendamento.objects.filter(
                    data_marcada__lt=pendulum.now(),
                    servico__disponivel_na_barbearia=barbearia,
                    agendamento_cancelado=False
                )
            )
            lucro_mensal = agendamentos.filter(
                data_marcada__month=pendulum.now().month 
            )
            financeiros = barbearia.financeiro_set.all()

            despesas = Decimal(sum(barbeiro.salario for barbeiro in barbeiros))
            lucro_planos = Decimal(sum(lucro.preco for lucro in planos))
            lucro_total = (Decimal(sum(lucro.preco_do_servico for lucro in agendamentos)) + lucro_planos) - despesas
            lucro_mes = Decimal(sum(lucro.preco_do_servico for lucro in lucro_mensal)) + lucro_planos
            receita = Decimal(sum(lucro.preco_do_servico for lucro in agendamentos))
            
            with transaction.atomic(): 
                for financeiro in financeiros:
                    financeiro.renda_mensal = lucro_mes
                    financeiro.despesas = despesas
                    financeiro.lucro_planos = lucro_planos
                    financeiro.lucro_total = lucro_total
                    financeiro.receita_total = receita 
                    financeiro.prejuizo = lucro_total < 0
                    financeiro.lucro = lucro_total > 0
                    financeiro.save()
    
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
        verbose_name = 'Finança'
        verbose_name_plural = 'Finanças'
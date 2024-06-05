from django.db import models, transaction
from django.db.models import Q

from ..models import Barbearia

class Financeiro(models.Model):
    barbearia = models.ForeignKey(
        Barbearia,
        verbose_name='Barbearia',
        on_delete=models.SET_NULL,
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
    
    def atualizar_financas(self, obj):
        from agendamentos.models import Agendamento
        from datetime import datetime
        
        barbearia = Barbearia.objects.get(id=obj.barbearia.id)
        barbeiros = barbearia.barbeiro_set.all()
        agendamentos = (
            Agendamento.objects.filter(
                data_marcada__lt=datetime.now(),
                servico__disponivel_na_barbearia=barbearia,
            )
        )
        lucro_mensal = agendamentos.filter(
            Q(data_marcada__lt=datetime.now()) &
            Q(data_marcada__month=datetime.now().month)
        )
        
        despesas = sum(barbeiro.salario for barbeiro in barbeiros)
        lucro_total = sum(lucro.preco_do_servico for lucro in agendamentos) - despesas
        lucro_mes = sum(lucro.preco_do_servico for lucro in lucro_mensal) - despesas
        receita = sum(lucro.preco_do_servico for lucro in agendamentos)
        
        with transaction.atomic():
            Financeiro.objects.update(
                barbearia=barbearia,
                renda_mensal=lucro_mes,
                despesas=despesas,
                lucro_total=lucro_total,
                receita_total=receita,
                prejuizo=True if lucro_mes < 0 else False,
                lucro=True if lucro_mes > 0 else False,
            )
        
    def limpar_financas(self, obj):
        financeiro = Financeiro.objects.get(id=obj.id)
        financeiro.renda_mensal = 0
        financeiro.despesas = 0
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
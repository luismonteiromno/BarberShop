from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import transaction

from agendamentos.models import (
    Agendamento,
    Servico
)

from ..models import (
    Barbearia,
    Financeiro
)

import pendulum
from datetime import datetime

@receiver(post_save, sender=Barbearia)
def registrar_lucros(sender, instance, created, **kwargs):
    barbearia = Barbearia.objects.get(pk=instance.id)
    barbeiros = barbearia.barbeiro_set.all()
    agendamentos = (
        Agendamento.objects.filter(
            data_marcada__lt=pendulum.now(),
            servico__disponivel_na_barbearia=barbearia,
        )
    )
    lucro_mensal = agendamentos.filter(
         data_marcada__month=pendulum.now().month 
    )
    
    despesas = sum(barbeiro.salario for barbeiro in barbeiros)
    lucro_total = sum(lucro.preco_do_servico for lucro in agendamentos) - despesas
    lucro_mes = sum(lucro.preco_do_servico for lucro in lucro_mensal)
    receita = sum(lucro.preco_do_servico for lucro in agendamentos)
        
    with transaction.atomic():
        if created:
            financeiro = Financeiro.objects.create(
                barbearia=barbearia,
                renda_mensal=lucro_mes,
                despesas=despesas,
                lucro_total=lucro_total,
                receita_total=receita,
                prejuizo=lucro_total < 0,
                lucro=lucro_total > 0
            )
        else:
            financeiro = Financeiro.objects.get(pk=barbearia.id)
            financeiro.renda_mensal = lucro_mes
            financeiro.despesas = despesas
            financeiro.lucro_total = lucro_total
            financeiro.receita_total = receita
            financeiro.prejuizo = lucro_total < 0
            financeiro.lucro = lucro_total > 0
            financeiro.save()
            
        
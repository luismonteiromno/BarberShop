import pendulum
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from agendamentos.models import Agendamento, Servico

from ..models import Barbearia, Barbeiro, Financeiro


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
        defaults = {
            "renda_mensal": lucro_mes,
            "despesas": despesas,
            "lucro_total": lucro_total,
            "receita_total": receita,
            "prejuizo": lucro_total < 0,
            "lucro": lucro_total > 0,
        }
        Financeiro.objects.update_or_create(
            barbearia=barbearia, 
            renda_mensal=lucro_mes,
            despesas=despesas,
            lucro_total=lucro_total,
            receita_total=receita,
            prejuizo=lucro_total < 0,
            lucro=lucro_total > 0,
            defaults=defaults
        )
            
# @receiver(post_save, sender=Barbeiro)
# def atualizar_lucros(sender, instance, created, **kwargs):
#     if created:
#         financeiro = Financeiro.objects.get(barbearia_id=instance.barbearia.id)
#         financeiro.despesas += instance.salario
#         financeiro.lucro_total -= instance.salario
#         financeiro.save()
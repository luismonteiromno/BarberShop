from decimal import Decimal
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction

from ..models import Agendamento, HistoricoDeAgendamento, MeuAgendamento
from barbearias.models import Cliente


@receiver(post_save, sender=Agendamento)
def agendamento_criado(sender, instance, created, **kwargs):
    cliente = Cliente.objects.get(cliente__email=instance.cliente)
    if created:
        with transaction.atomic():
            HistoricoDeAgendamento.objects.create(
                servico_fornecido=instance.servico,
                preco_do_servico=instance.preco_do_servico,
                cliente=cliente,
                barbeiro=instance.escolher_barbeiro,
                data_do_agendamento=instance.data_marcada,
            )
            cliente.credito = Decimal(0)
            cliente.save()
        
        
@receiver(post_save, sender=Agendamento)
def meu_agendamento(sender, instance, created, **kwargs):
    cliente = Cliente.objects.get(cliente__email=instance.cliente)
    if created:
        with transaction.atomic():
            MeuAgendamento.objects.create(
                agendamento=instance,
                cliente=cliente,
            )
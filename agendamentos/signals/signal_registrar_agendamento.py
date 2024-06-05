from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models import Agendamento, HistoricoDeAgendamento


@receiver(post_save, sender=Agendamento)
def agendamento_criado(sender, instance, created, **kwargs):
    if created:
        HistoricoDeAgendamento.objects.create(
            servico_fornecido=instance.servico,
            preco_do_servico=instance.preco_do_servico,
            cliente=instance.usuario,
            barbeiro=instance.escolher_barbeiro,
            data_do_agendamento=instance.data_marcada,
        ) 
    print('teste')

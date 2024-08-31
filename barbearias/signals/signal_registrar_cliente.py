from decimal import Decimal

from crum import get_current_user
from django.db import transaction
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from agendamentos.models import Agendamento

from ..models import Cliente, PlanosDeFidelidade


@receiver(post_save, sender=Cliente)
def registrar_cliente_plano_de_fidelidade(sender, instance, created, **kwargs):
    planos = PlanosDeFidelidade.objects.filter(
        nome=instance.plano_de_fidelidade
    )
    with transaction.atomic():
        if created:
            for plano in planos:
                plano.usuarios += 1
                plano.save()
        else:
            return

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import transaction

from ..models import (
    Cliente,
    PlanosDeFidelidade
)

@receiver(post_save, sender=Cliente)
def registrar_cliente(sender, instance, created, **kwargs):
    planos = PlanosDeFidelidade.objects.filter(
        nome=instance.plano_de_fidelidade
    )
    ...
    with transaction.atomic():
        if created:
            for plano in planos:
                plano.usuarios += 1
                plano.save()
        else:
            for plano in planos:
                plano.usuarios += 0
                plano.save()
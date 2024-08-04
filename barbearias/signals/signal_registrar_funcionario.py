from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models import Barbearia, Barbeiro


@receiver(post_save, sender=Barbeiro)
def registrar_funcionario(sender, instance, created, **kwargs):
    for barbearia in instance.barbearias.all():
        barbearia_que_trabalha = Barbearia.objects.get(pk=barbearia.id)
        barbearia_que_trabalha.barbeiros.add(instance.id)

from django.dispatch import receiver
from django.db.models.signals import post_save


from ..models import (
    Barbearia,
    Barbeiro
)


@receiver(post_save, sender=Barbeiro)
def registrar_funcionario(sender, instance, created, **kwargs):
    if created:
        barbearia = Barbearia.objects.get(id=instance.barbearia.id)
        barbearia.funcionarios.add(instance.id)
    else:
        barbearia = Barbearia.objects.get(id=instance.barbearia.id)
        barbearia.funcionarios.add(instance.id)
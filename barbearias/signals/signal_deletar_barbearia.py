from django.db.models.signals import pre_delete
from django.dispatch import receiver

from ..models import (
    Avaliacao,
    Barbearia,
    Contato,
    Financeiro,
    Funcionario,
    PlanosDeFidelidade,
)


@receiver(pre_delete, sender=Barbearia)
def deletar_avaliacao(sender, instance, using, **kwargs):
    Avaliacao.objects.filter(barbearia=instance).delete()


@receiver(pre_delete, sender=Barbearia)
def deletar_contato(sender, instance, using, **kwargs):
    Contato.objects.filter(barbeiro=instance).delete()


@receiver(pre_delete, sender=Barbearia)
def deletar_financeiro(sender, instance, using, **kwargs):
    Financeiro.objects.filter(barbearia=instance).delete()


@receiver(pre_delete, sender=Barbearia)
def deletar_funcionario(sender, instance, using, **kwargs):
    Funcionario.objects.filter(barbearias=instance).delete()


@receiver(pre_delete, sender=Barbearia)
def deletar_plano_de_fidelidade(sender, instance, using, **kwargs):
    PlanosDeFidelidade.objects.filter(funcionario=instance).delete()

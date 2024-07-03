from django.dispatch import receiver
from django.db.models import Avg
from django.db.models.signals import post_save

from ..models import AvaliacaoDoBarbeiro, Barbeiro


@receiver(post_save, sender=AvaliacaoDoBarbeiro)
def atualizar_avaliacao(sender, created, instance, **kwargs):
    barbeiro = Barbeiro.objects.get(id=instance.barbeiro.id)
    barbeiro.avaliacao = barbeiro.barbeiro_avaliacao.aggregate(
        media_avaliacao=Avg('avaliacao')
    )['media_avaliacao']
    barbeiro.save()

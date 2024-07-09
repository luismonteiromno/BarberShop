from django.dispatch import receiver
from django.db.models import Avg
from django.db.models.signals import post_save

from ..models import Avaliacao, Barbearia


@receiver(post_save, sender=Avaliacao)
def atualizar_avaliacao(sender, created, instance, **kwargs):
    barbearia = Barbearia.objects.get(id=instance.barbearia.id)
    barbearia.avaliacao = barbearia.avaliacao_set.aggregate(
        media_avaliacao=Avg('avaliacao')
    )['media_avaliacao']
    barbearia.save()

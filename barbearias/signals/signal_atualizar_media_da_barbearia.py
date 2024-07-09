from django.dispatch import receiver
from django.db.models import Avg
from django.db.models.signals import post_save
from django.db import connection

from ..models import Avaliacao, Barbearia

@receiver(post_save, sender=Avaliacao)
def atualizar_media_da_barbearia(sender, instance, created, **kwargs):
    if created:
        barbearia = Barbearia.objects.get(id=instance.barbearia.id)
        barbearia.media_das_avaliacoes = barbearia.avaliacao_set.aggregate(
            media_avaliacao=Avg('avaliacao')
        )['media_avaliacao']
        barbearia.save()

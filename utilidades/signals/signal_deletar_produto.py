from django.db.models.signals import pre_delete, pre_delete
from django.dispatch import receiver

from barbearias.models import Barbearia

from ..models import Aviso, Produto, Promocao


@receiver(pre_delete, sender=Barbearia)
def deletar_produto(sender, instance, using, **kwargs):
    Produto.objects.filter(barbearia=instance).delete()


@receiver(pre_delete, sender=Barbearia)
def deletar_aviso(sender, instance, using, **kwargs):
    Aviso.objects.filter(barbearia=instance).delete()


@receiver(pre_delete, sender=Barbearia)
def deletar_promocao(sender, instance, using, **kwargs):
    Promocao.objects.filter(barbearia=instance).delete()


@receiver(pre_delete, sender=Produto)
def deletar_promocao_do_produto(sender, instance, using, **kwargs):
    Promocao.objects.filter(produto=instance).delete()

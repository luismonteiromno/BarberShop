from django.db import transaction
from django.dispatch import receiver
from django.db.models.signals import post_save

import secrets
from ..models import Compra, NotaFiscal

@receiver(post_save, sender=Compra)
def emitir_nota_fiscal(sender, instance, created, **kwargs):
    if created:
        nota_fiscal = secrets.token_hex(32)
        with transaction.atomic():
            NotaFiscal.objects.create(
                cliente=instance.cliente,
                produto=instance.produto,
                numero=f'NF-{nota_fiscal}',
                data_emissao=instance.data_compra,
                valor_total=instance.preco_total
            )

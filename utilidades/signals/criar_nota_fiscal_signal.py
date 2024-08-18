import secrets

from django.db import transaction
from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models import Compra, NotaFiscal, Produto


@receiver(post_save, sender=Compra)
def emitir_nota_fiscal(sender, instance, created, **kwargs):
    if created:
        nota_fiscal = secrets.token_hex(32)
        with transaction.atomic():
            NotaFiscal.objects.create(
                cliente=instance.cliente,
                produto=instance.produto,
                quantidade_comprada=instance.quantidade,
                numero=f'NF-{nota_fiscal}',
                data_emissao=instance.data_da_compra,
                valor_unitario=instance.preco_unitario,
                valor_total=instance.preco_total,
            )
            Produto.objects.filter(id=instance.produto.id).update(
                quantidade=F('quantidade') - instance.quantidade
            )

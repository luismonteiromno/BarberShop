import secrets

from django.db import transaction
from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models import Compra, NotaFiscal, Produto


@receiver(post_save, sender=Compra)
def emitir_nota_fiscal(sender, instance, created, **kwargs):
    if created:
        nota_fiscal_token = secrets.token_hex(32)
        with transaction.atomic():
            nota_fiscal = NotaFiscal.objects.create(
                barbearia=instance.produto.barbearia,
                cliente=instance.cliente,
                compra=instance,
                produto=instance.produto,
                quantidade_comprada=instance.quantidade,
                numero=f'NF-{nota_fiscal_token}',
                data_emissao=instance.data_da_compra,
                valor_unitario=instance.preco_unitario,
                valor_total=instance.preco_total,
            )

            Compra.objects.filter(id=instance.id).update(
                nota_fiscal=nota_fiscal
            )

            Produto.objects.filter(id=instance.produto.id).update(
                quantidade=F('quantidade') - instance.quantidade
            )
    else:
        NotaFiscal.objects.filter(compra=instance).update(
            status=instance.status
        )

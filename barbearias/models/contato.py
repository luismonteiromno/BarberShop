from django.db import models

from . import Barbearia


class Contato(models.Model):
    barbearia = models.ForeignKey(
        Barbearia,
        verbose_name='Barbearia',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='contatos'
    )
    
    contato = models.CharField(
        'Contato',
        max_length=100,
        blank=True,
        null=True
    )
    
    link_para_contato = models.URLField(
        'Link para contato',
        max_length=100,
        blank=True,
        null=True
    )
    
    def __str__(self):
        return self.contato
    
    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
        
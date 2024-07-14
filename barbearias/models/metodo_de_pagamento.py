from django.db import models

class MetodoDePagamento(models.Model):
    metodo_de_pagamento = models.CharField(
        'Método de pagamento',
        max_length=100,
    )
    
    def __str__(self):
        return self.metodo_de_pagamento
    
    class Meta:
        verbose_name = 'Método de Pagamento'
        verbose_name_plural = 'Métodos de Pagamento'

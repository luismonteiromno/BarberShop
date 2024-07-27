from ..models import MetodoDePagamento
from django.contrib import admin


@admin.register(MetodoDePagamento)
class MetodoDePagamentoAdmin(admin.ModelAdmin):
    list_display = [
        'metodo_de_pagamento',
    ]

    search_fields = [
        'metodo_de_pagamento',
    ]

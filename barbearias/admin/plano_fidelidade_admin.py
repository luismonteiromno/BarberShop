from typing import Any
from django.contrib import admin
from django.http import HttpRequest

from ..models import PlanosDeFidelidade
from .cliente_inline import ClienteInline
from rangefilter.filters import (
    DateRangeFilterBuilder,
    DateTimeRangeFilterBuilder,
    NumericRangeFilterBuilder,
    DateRangeQuickSelectListFilterBuilder,
)


@admin.register(PlanosDeFidelidade)
class PlanosDeFidelidadeAdmin(admin.ModelAdmin):
    list_display = [
        'barbearia',
        'nome',
        'preco',
    ]
    
    search_fields = [
        'nome'
        'barbearia__nome_da_barbearia'
    ]
    
    exclude = [
        'quantidade_de_cortes'
    ]
    
    autocomplete_fields = [
        'barbearia'
    ]
    
    list_filter = [
        ('usuarios', NumericRangeFilterBuilder())
    ]
    
    readonly_fields = [
        'usuarios',
    ]
    
    inlines = [
        ClienteInline,
    ]
    
    filter_horizontal = ['metodo_de_pagamento']
    
    def get_readonly_fields(self, request, obj):
        if not request.user.is_superuser:
            return self.readonly_fields + ['metodo_de_pagamento']
        return super().get_readonly_fields(request, obj)

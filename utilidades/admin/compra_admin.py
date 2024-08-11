from typing import Any
from django.contrib import admin
from django.http import HttpRequest

from ..models import Compra


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'cliente',
        'produto'
    ]

    search_fields = [
        'id',
        'cliente',
        'produto'
    ]
    
    autocomplete_fields = [
        'cliente',
        'produto'
    ]
    
    readonly_fields = [
        'preco_total'
    ]

    def get_readonly_fields(self, request, obj):
        if obj:
            return self.readonly_fields + ['quantidade']
        return super().get_readonly_fields(request, obj)

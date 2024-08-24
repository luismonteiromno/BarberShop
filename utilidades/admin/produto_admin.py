from typing import Any
from admin_auto_filters.filters import AutocompleteFilter
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from rangefilter.filters import NumericRangeFilter

from agendamentos.admin.servico_admin import BarbeariaFilter

from ..models import Produto


class BarbeariaFilter(AutocompleteFilter):
    title = 'Barbearia'
    field_name = 'barbearia'


class CategoriaDoServicoFilter(AutocompleteFilter):
    title = 'Tipo do Produto'
    field_name = 'tipo_do_produto'


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
        'preco',
        'tipo_do_produto',
        'quantidade',
    ]

    search_fields = [
        'nome',
        'tipo_do_produto__nome',
    ]

    autocomplete_fields = [
        'barbearia',
        'tipo_do_produto',
    ]

    list_filter = [
        BarbeariaFilter,
        CategoriaDoServicoFilter,
        ('quantidade', NumericRangeFilter),
    ]
    
    list_editable = ['quantidade']

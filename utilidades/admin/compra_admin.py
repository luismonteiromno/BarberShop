from django.contrib import admin
from admin_auto_filters.filters import AutocompleteFilter

from ..models import Compra

class ClienteAutoCompleteFilter(AutocompleteFilter):
    title = 'Cliente'
    field_name = 'cliente'

class ProdutoAutoCompleteFilter(AutocompleteFilter):
    title = 'Produto'
    field_name = 'produto'

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'cliente',
        'preco_total',
        'preco_unitario',
        'produto'
    ]

    search_fields = [
        'id',
        'cliente',
        'produto'
    ]
    
    list_filters = [
        ClienteAutoCompleteFilter,
        ProdutoAutoCompleteFilter,
    ]
    
    autocomplete_fields = [
        'cliente',
        'produto'
    ]
    
    readonly_fields = [
        'cliente',
        'nota_fiscal',
        'preco_unitario',
        'preco_total',
    ]

    def get_readonly_fields(self, request, obj):
        if obj:
            return self.readonly_fields + ['quantidade', 'produto']
        if not obj:
            return self.readonly_fields + ['status']
        return super().get_readonly_fields(request, obj)
    
    def get_search_results(self, request, queryset, search_term):
        # Filtra apenas produtos com quantidade maior que 0
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        queryset = queryset.filter(quantidade__gt=0)
        return queryset, use_distinct

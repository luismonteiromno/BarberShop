from django.contrib import admin
from admin_auto_filters.filters import AutocompleteFilter

from ..models import NotaFiscal


class ClienteFilter(AutocompleteFilter):
    title = 'Cliente'
    field_name = 'cliente'

@admin.register(NotaFiscal)
class NotaFiscalAdmin(admin.ModelAdmin):
    list_display = [
        'numero',
        'cliente'
    ]

    search_fields = [
        'numero',
        'cliente__nome'
    ]
    
    autocomplete_fields = [
        'cliente',
        'produto'
    ]
    
    list_filter = [
        ClienteFilter,
    ]
    
    def has_add_permission(self, request, obj=None) -> bool:
        return False
    
    def has_change_permission(self, request, obj=None) -> bool:
        return False
    
    def has_delete_permission(self, request, obj=None) -> bool:
        return False

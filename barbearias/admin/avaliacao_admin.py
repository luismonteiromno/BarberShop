from django.contrib import admin
from admin_auto_filters.filters import AutocompleteFilter

from ..models import Avaliacao


class BarbeariaFilter(AutocompleteFilter):
    title = 'Barbearia'
    field_name = 'barbearia'

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = [
        'avaliacao',
        'barbearia',
        'usuario',
    ]
    
    autocomplete_fields = [
        'barbearia'
    ]
    
    list_filter = [
        BarbeariaFilter,
    ]
    
    readonly_fields = [
        'usuario'
    ]
    
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ['barbearia']
        else:
            return self.readonly_fields
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def save_form(self, request, form, change):
        print('teste')
        return super().save_form(request, form, change)
    
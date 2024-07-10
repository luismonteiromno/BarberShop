from django.contrib import admin
from admin_auto_filters.filters import AutocompleteFilter


from ..models import AvaliacaoDoBarbeiro


class BarbeiroFilter(AutocompleteFilter):
    title = 'Barbeiro'
    field_name = 'barbeiro'

@admin.register(AvaliacaoDoBarbeiro)
class AvaliacaoDoBarbeiroAdmin(admin.ModelAdmin):
    list_display = [
        'barbeiro',
        'avaliacao',
    ]
    
    search_fields = [
        'barbeiro__barbeiro__username',
        'barbeiro__barbearia__nome_da_barbearia'
    ]
    
    list_filter = [
        BarbeiroFilter
    ]
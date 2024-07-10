from django.contrib import admin
from admin_auto_filters.filters import AutocompleteFilter

from ..models import Promocao

class ServicoFilter(AutocompleteFilter):
    title = 'Serviço'
    field_name ='servico'  

class PlanoFidelidadeFilter(AutocompleteFilter):
    title = 'Plano Fidelidade'
    field_name = 'plano_fidelidade'

@admin.register(Promocao)
class PromocaoAdmin(admin.ModelAdmin):
    list_display = [
        'servico',
        'nome_da_promocao',
        'inicio_da_promocao',
        'fim_da_promocao',
    ]
    
    fields = [
        'servico',
        'plano_fidelidade',
        'nome_da_promocao',
        'inicio_da_promocao',
        'fim_da_promocao',
    ]
    
    list_filter = [
        ServicoFilter,
        PlanoFidelidadeFilter,
    ]
    
    autocomplete_fields = [
        'servico',
        'plano_fidelidade',
    ]
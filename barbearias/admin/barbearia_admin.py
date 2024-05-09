from django.contrib import admin
from .avaliacao_inline import AvaliacaoInline

from agendamentos.admin.servico_inline import ServicoInline

from ..models import Barbearia

from .barbeiro_inline import BarbeiroInline

@admin.register(Barbearia)
class BarbeariaAdmin(admin.ModelAdmin):
    list_display = [
        'nome_da_barbearia',
        'cnpj',
    ]
    
    autocomplete_fields = [
        'dono'
    ]
    
    list_select_related = [
        'dono'
    ]
    
    filter_horizontal = [
        'funcionarios'
    ]
    
    search_fields = [
        'nome_da_barbearia',
        'cnpj',
    ]
    
    readonly_fields = [
        'dono'
    ]

    inlines = [
        AvaliacaoInline,
        BarbeiroInline,
        ServicoInline,
    ]
    
   
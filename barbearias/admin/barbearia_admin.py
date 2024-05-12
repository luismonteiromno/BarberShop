from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django_object_actions import DjangoObjectActions

from .avaliacao_inline import AvaliacaoInline

from agendamentos.admin.servico_inline import ServicoInline

from ..models import Barbearia

from .barbeiro_inline import BarbeiroInline

@admin.register(Barbearia)
class BarbeariaAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = [
        'nome_da_barbearia',
        'dono',
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
    
    change_actions = [
        'instancia'
    ]
    
    # actions = [
    #     'ola'
    # ]
    
    changelist_actions = [
        'instancia'
    ]
    
    def instancia(self, request, obj):
        print(request.user)
        print(obj)
        print('olja')
    
   
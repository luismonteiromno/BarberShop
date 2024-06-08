from typing import Any

from agendamentos.admin.servico_inline import ServicoInline
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django_object_actions import DjangoObjectActions
from import_export.admin import ImportExportModelAdmin

from ..models import Barbearia, Financeiro
from .avaliacao_inline import AvaliacaoInline
from .barbeiro_inline import BarbeiroInline
from .contato_inline import ContatoInline
from .financeiro_inline import FinanceiroInline

@admin.register(Barbearia)
class BarbeariaAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = [
        'nome_da_barbearia',
        'dono',
        'quantidade_de_agendamentos',
        'ultimo_agendamento',
        'numero_de_contatos',
        'avisos_recentes',
        'ultima_avaliacao',
        'media_das_avaliacoes_0_a_5'
    ]
    
    fieldsets = [
        ['Informações', {
            'fields': [
                'nome_da_barbearia',
                'dono',
                'cnpj',
                'funcionarios',
                'rua',
                'bairro',
                'complemento',
                'cidade',
                'estado',
                'cep',
            ]
        }],
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
        'dono',
    ]

    inlines = [
        AvaliacaoInline,
        BarbeiroInline,
        ContatoInline,
        FinanceiroInline,
        ServicoInline,
    ]
    
    # change_actions = [
    #     'atualizar_financas'
    # ]
    
    # actions = [
    #     'ola'
    # ]
        
    changelist_actions = [
        'atualizar_todas_as_financas'
    ]
    
    def atualizar_todas_as_financas(self, request, obj):
        Financeiro.atualizar_todas_as_financas(self, obj)
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        
        if not request.user.is_superuser:
            queryset = queryset.filter(dono=request.user)
            
        return queryset
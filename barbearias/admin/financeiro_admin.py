from django.contrib import admin
from django_object_actions import DjangoObjectActions
from admin_auto_filters.filters import AutocompleteFilter
from import_export.admin import ImportExportModelAdmin

from ..models import Financeiro

class BarbeariaFilter(AutocompleteFilter):
    title = 'Barbearia'
    field_name = 'barbearia'

@admin.register(Financeiro)
class FinanceiroAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = [
        'barbearia',
        'lucro_total',
        'receita_total',
        'despesas',
    ]
    
    fieldsets = [
        ['Financeiro',
            {
                'fields': [
                    'barbearia',
                    'lucro_total',
                    'receita_total',
                    'lucro_planos',
                    'despesas',
                ]
            }
        ],
        ['Lucros Mensais',
            {
                'fields': [
                    'lucro_mes_anterior',
                    'renda_mensal',
                    'comparar_lucros_mes_anterior_e_atual',
                    'comparar_lucros_mes_anterior_e_atual_porcentagem',
                    'prejuizo',
                    'lucro',
                ]
            }
        ],
    ]
    
    autocomplete_fields = [
        'barbearia',
    ]
    
    list_filter = [
        BarbeariaFilter,
    ]
  
    change_actions = [
        'atualizar_financas',
        'limpar_financeiro',
    ]
    
    changelist_actions = [
        'atualizar_todos_os_financeiros'
    ]
    
    def atualizar_todos_os_financeiros(self, request, obj):
        # Financeiro.atualizar_todas_as_financas(self, obj)
        Financeiro().atualizar_todas_as_financas(obj)
    
    def atualizar_financas(self, request, obj):
        Financeiro().atualizar_financas(obj)
    
    def limpar_financeiro(self, request, obj):
        Financeiro().limpar_financeiro(obj)
    
    def has_add_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
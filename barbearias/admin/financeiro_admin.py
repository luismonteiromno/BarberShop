from django.contrib import admin
from django_object_actions import DjangoObjectActions
from import_export.admin import ImportExportModelAdmin
from ..models import Financeiro

@admin.register(Financeiro)
class FinanceiroAdmin(DjangoObjectActions, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [
        'barbearia',
        'lucro_total',
        'receita_total',
        'despesas',
    ]
    
    change_actions = [
        'atualizar_financas',
        'limpar_financeiro',
    ]
    
    def atualizar_financas(self, request, obj):
        Financeiro.atualizar_financas(self, obj)
    
    def limpar_financeiro(self, request, obj):
        Financeiro.limpar_financeiro(self, obj)
    
    def has_add_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
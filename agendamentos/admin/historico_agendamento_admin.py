from django.contrib import admin
from ..models import HistoricoDeAgendamento

@admin.register(HistoricoDeAgendamento)
class HistoricoDeAgendamentoAdmin(admin.ModelAdmin):
    list_display = [
        'servico_fornecido',
        'preco_do_servico',
        'cliente',
        'barbeiro',
        'data_do_agendamento',
    ]
    
    readonly_fields = [
        'preco_do_servico'
    ]
    
    list_filter = [
        'barbeiro',
        'servico_fornecido',
    ]
    
    def has_add_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
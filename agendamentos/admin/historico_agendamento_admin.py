from django.contrib import admin, messages
from django_object_actions import DjangoObjectActions

from ..models import HistoricoDeAgendamento

@admin.register(HistoricoDeAgendamento)
class HistoricoDeAgendamentoAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = [
        'servico_fornecido',
        'preco_do_servico',
        'cliente',
        'barbeiro',
        'data_do_agendamento',
        'barbearia',
    ]
    
    list_filter = [
        'barbeiro',
        'servico_fornecido',
        'servico_fornecido__disponivel_na_barbearia'
    ]
    
    changelist_actions = [
        'deletar_historico'
    ]
    
    def deletar_historico(self, request, obj):
        if obj:
            obj.delete()
            self.message_user(request, 'Histórico de agendamento deletado com sucesso!', level=messages.SUCCESS)
        else:
            self.message_user(request, 'Histórico de agendamento está vazio!', level=messages.WARNING)
    
    def has_add_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        
        if not request.user.is_superuser:
            queryset = queryset.filter(
                barbearia__dono=request.user
            ).select_related('barbearia__dono')
            
        return queryset
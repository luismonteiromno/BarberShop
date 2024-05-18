from django.contrib import admin
from django_object_actions import DjangoObjectActions
from datetime import datetime

from ..models import Agendamento


from django.contrib.auth.models import User

@admin.register(Agendamento)
class AgendamentoAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = [
        'usuario',
        'servico',
        'data_marcada',
    ]
    
    autocomplete_fields = [
        'servico'
    ]
    
    readonly_fields = [
        'usuario',
        'preco_do_servico'
    ]
    
    changelist_actions = [
        'excluir_agendamentos_passados'
    ]
    
    def excluir_agendamentos_passados(self, request, obj):
        for instance in obj:
            data_atual = datetime.strftime(datetime.now(), '%d/%m/%Y %H:%M:%S')
            data_marcada = datetime.strftime(instance.data_marcada, '%d/%m/%Y %H:%M:%S')
            if data_atual >= data_marcada:
                instance.delete()
                self.message_user(request, 'Histórico de agendamento deletado com sucesso!')

    
    def formfield_for_foreignkey(self, db_field, request,**kwargs):
        if db_field.name == 'escolher_barbeiro':
            kwargs['queryset'] = User.objects.filter(profile__tipo_do_usuario='Barbeiro')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

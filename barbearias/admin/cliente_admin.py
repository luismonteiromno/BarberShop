from django.contrib import admin, messages
from django_object_actions import DjangoObjectActions
from admin_auto_filters.filters import AutocompleteFilter

from ..models import Cliente


class ClienteFilter(AutocompleteFilter):
    title = 'Plano de Fidelidade'
    field_name = 'plano_de_fidelidade'

@admin.register(Cliente)
class ClienteAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = [
        'cliente',
        'plano_de_fidelidade',
    ]
    
    autocomplete_fields = [
        'cliente',
        'plano_de_fidelidade',
    ]
    
    list_select_related = ['cliente']
    
    list_filter = [
        ClienteFilter,
    ]
    
    readonly_fields = [
        'cliente',
        'credito'
    ]
    
    change_actions = [
        'atualizar_credito'
    ]
    
    changelist_actions = [
        'atualizar_creditos'
    ]
    
    def atualizar_credito(self, request, obj):
        Cliente().atualizar_credito_cliente(obj)
        if obj.credito == 50:
            self.message_user(
                request,
                "O cliente já possui o crédito máximo",
                level=messages.WARNING
            )
        else:
            self.message_user(
                request,
                "O crédito foi atualizado com sucesso",
                level=messages.SUCCESS
            )
    
    def atualizar_creditos(self, request, obj):
        Cliente().atualizar_credito_cliente(obj)
        for instancia in obj:
            if instancia.credito == 50:
                self.message_user(
                    request,
                    f"O cliente {instancia.cliente} já possui o crédito máximo",
                    level=messages.WARNING
                )
            else:
                self.message_user(
                    request,
                    "Todos os créditos foram atualizados com sucesso",
                    level=messages.SUCCESS
                )
    
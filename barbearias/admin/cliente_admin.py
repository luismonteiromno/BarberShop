from typing import Any
from django.contrib.auth.models import User
from django.contrib import admin, messages
from django.db.models.fields.related import ForeignKey
from django.forms.models import ModelChoiceField
from django.http import HttpRequest
from django_object_actions import DjangoObjectActions
from admin_auto_filters.filters import AutocompleteFilter

from ..models import Cliente

from .cartao_inline import CartaoInline
from .chave_pix_inline import ChavePixInline

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
        # 'cliente',
        'plano_de_fidelidade',
    ]
    
    list_select_related = ['cliente']
    
    list_filter = [
        ClienteFilter,
    ]
    
    readonly_fields = [
        # 'cliente',
        'credito'
    ]
    
    change_actions = [
        'atualizar_credito',
        'gerar_chave_aleatoria'
    ]
    
    changelist_actions = [
        'atualizar_creditos'
    ]
    
    inlines = [
        CartaoInline,
        ChavePixInline
    ]
    
    def gerar_chave_aleatoria(self, request, obj):
        try:
            Cliente().gerar_chave_aleatoria(obj)
        except:
            self.message_user(
                request,
                "Você só pode ter UMA chave PIX aleatória!",
                level=messages.WARNING
            )
    gerar_chave_aleatoria.label = 'Gerar Chave Aleatória'
    
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
                
    def formfield_for_foreignkey(self, db_field, request,  **kwargs):
        from django.db.models import Q
        if db_field.name == 'cliente':
            kwargs['queryset'] = User.objects.filter(
               ~Q(profile__tipo_do_usuario='Barbeiro')
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
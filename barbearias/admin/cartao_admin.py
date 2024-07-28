from typing import Any
from django.contrib import admin, messages
from django.http import HttpRequest
from django_object_actions import DjangoObjectActions
from ..models import Cartao

from admin_auto_filters.filters import AutocompleteFilter

class TitularFilter(AutocompleteFilter):
    title = 'Titular'
    field_name = 'titular'


@admin.register(Cartao)
class CartaoAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = [
        'titular',
        'tipo_do_cartao'
    ]

    search_fields = [
        'titular__nome',
        'numero',
    ]

    autocomplete_fields = [
        'titular',
    ]
    
    list_filter = [
        TitularFilter,
    ]
    
    list_select_related = ['titular']
    
    readonly_fields = [
        'cartao_bloqueado',
        'data_de_criacao',
        'data_de_atualizacao'
    ]
    
    change_actions = [
        'bloquear_cartao',
        'desbloquear_cartao',
    ]
    
    def bloquear_cartao(self, request, obj):
        if obj.cartao_bloqueado:
            self.message_user(
                request,
                'O cartão já está bloqueado!',
                level=messages.SUCCESS
            )
        else:
            obj.cartao_bloqueado = True
            obj.save()
            self.message_user(
                request,
                'Cartão bloqueado com sucesso!',
                level=messages.SUCCESS
            )
        
    def desbloquear_cartao(self, request, obj):
        if not obj.cartao_bloqueado:
            self.message_user(
                request,
                'O cartão já está desbloqueado!',
                level=messages.SUCCESS
            )
        else:
            obj.cartao_bloqueado = False
            obj.save()
            self.message_user(
                request,
                'Cartão desbloqueado com sucesso!',
                level=messages.SUCCESS
            )

    def get_readonly_fields(self, request, obj):
        if obj:
            return self.readonly_fields + ['validade']
        return super().get_readonly_fields(request, obj)

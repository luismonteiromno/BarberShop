from datetime import datetime
from typing import Any

from django.contrib import admin, messages
from django.contrib.auth.models import User
from django.db.models import Q
from django_object_actions import DjangoObjectActions

from ..forms import AgendamentoForm
from ..models import Agendamento


@admin.register(Agendamento)
class AgendamentoAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = [
        'id',
        'numero_do_agendamento',
        'cliente',
        'data_marcada',
    ]

    autocomplete_fields = ['servico']

    readonly_fields = [
        'numero_do_agendamento',
        'cliente',
        'desconto_do_usuario',
        'preco_do_servico',
        'agendamento_cancelado',
    ]

    form = AgendamentoForm

    # changelist_actions = [
    #     'excluir_agendamentos_passados'
    # ]

    # def excluir_agendamentos_passados(self, request, obj):
    #     for instance in obj:
    #         data_atual = datetime.strftime(datetime.now(), '%d/%m/%Y %H:%M:%S')
    #         data_marcada = datetime.strftime(instance.data_marcada, '%d/%m/%Y %H:%M:%S')
    #         if data_atual >= data_marcada:
    #             instance.delete()
    #             self.message_user(request, 'Agendamentos deletados com sucesso!', level=messages.SUCCESS)
    #             break
    #         else:
    #             self.message_user(request, 'Nenhum agendamento passado foi encontrado!', level=messages.WARNING)
    #             break

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'escolher_barbeiro':
            kwargs['queryset'] = User.objects.filter(
                profile__tipo_do_usuario='Barbeiro'
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        now = datetime.now()
        queryset = super().get_queryset(request)

        if not request.user.is_superuser:
            queryset = queryset.filter(
                servico__disponivel_na_barbearia__dono=request.user,
                agendamento_cancelado=False,
            ).select_related('servico__disponivel_na_barbearia__dono')

        return queryset.exclude(Q(data_marcada__lt=now) | Q(agendamento_cancelado=True))

from datetime import datetime

from django.contrib import admin, messages
from django_object_actions import DjangoObjectActions

from ..models import HistoricoDeAgendamento
from admin_auto_filters.filters import AutocompleteFilter


class BarbeiroFilter(AutocompleteFilter):
    title = 'Barbeiro'
    field_name = 'barbeiro'


class ServicoFilter(AutocompleteFilter):
    title = 'Nome do Serviço'
    field_name = 'servico_fornecido'


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

    search_fields = [
        'servico_fornecido__disponivel_na_barbearia__nome_da_barbearia'
    ]

    list_filter = [
        BarbeiroFilter,
        ServicoFilter,
    ]

    list_select_related = True

    search_help_text = 'Digite o nome das Barbearias para buscar os serviços'

    changelist_actions = ['deletar_historico']

    def deletar_historico(self, request, obj):
        if obj:
            for instance in obj:
                agora = datetime.now().strftime('%d/%m/%Y %H:%M')
                data_de_agendamento = instance.data_do_agendamento.strftime(
                    '%d/%m/%Y %H:%M'
                )
                if agora > data_de_agendamento:
                    instance.delete()
                    self.message_user(
                        request,
                        'Histórico de agendamento deletado com sucesso!',
                        level=messages.SUCCESS,
                    )
                else:
                    self.message_user(
                        request,
                        'Todos os agendamentos passados foram limpos!',
                        level=messages.INFO,
                    )
                    break
        else:
            self.message_user(
                request,
                'Histórico de agendamento está vazio!',
                level=messages.WARNING,
            )

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_queryset(self, request):
        from django.db.models import Q

        queryset = super().get_queryset(request)

        hoje = datetime.now()

        if not request.user.is_superuser:
            queryset = (
                queryset.filter(barbearia__dono=request.user)
                .select_related('barbearia__dono')
                .exclude(
                    Q(data_do_agendamento__lt=hoje)
                    | Q(agendamento_cancelado=True)
                )
            )

        return queryset

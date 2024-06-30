from django.contrib import admin, messages
from django_object_actions import DjangoObjectActions

from ..models import MeuAgendamento


@admin.register(MeuAgendamento)
class MeuAgendamentoAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = [
        "agendamento",
        "cliente",
        "servico",
        "cancelar_agendamento",
    ]

    fieldsets = [
        [
            "Detalhes do agendamento",
            {"fields": ["agendamento", "cliente", "cancelar_agendamento"]},
        ]
    ]

    readonly_fields = ["agendamento", "cliente", "cancelar_agendamento"]

    change_actions = ["cancelar_o_agendamento"]

    def cancelar_o_agendamento(self, request, obj):
        MeuAgendamento.cancelar_o_agendamento(self, obj)
        self.message_user(
            request, 
            "Agendamento cancelado com sucesso!", 
            level=messages.SUCCESS
        )

    def get_queryset(self, request):
        import pendulum

        queryset = super().get_queryset(request)

        if not request.user.is_superuser:
            queryset = queryset.filter(
                agendamento__data_marcada__gt=pendulum.now(), cliente=request.user
            )

        return queryset

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

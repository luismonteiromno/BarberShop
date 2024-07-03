from io import BytesIO

import nested_admin
import pandas as pd
from django.contrib import admin, messages
from django.db import transaction
from django.db.models import Q
from django_object_actions import DjangoObjectActions
from import_export.admin import ImportExportModelAdmin

from agendamentos.admin.servico_inline import ServicoInline

from ..models import Barbearia, Financeiro
from .avaliacao_inline import AvaliacaoInline
from .barbeiro_inline import BarbeiroInline
from .contato_inline import ContatoInline
from .financeiro_inline import FinanceiroInline
from .funcionario_inline import FuncionarioInline
from .plano_fidelidade_inline import PlanosDeFidelidadeInline


@admin.register(Barbearia)
class BarbeariaAdmin(DjangoObjectActions, nested_admin.NestedModelAdmin):
    list_display = [
        "nome_da_barbearia",
        "dono",
        "quantidade_de_agendamentos",
        "orcamento",
        "ultimo_agendamento",
        "numero_de_contatos",
        "avisos_recentes",
        "ultima_avaliacao",
        "media_das_avaliacoes_0_a_5",
    ]

    fieldsets = [
        [
            "Informações",
            {
                "fields": [
                    "nome_da_barbearia",
                    "dono",
                    "cnpj",
                    "funcionarios",
                    "rua",
                    "bairro",
                    "complemento",
                    "cidade",
                    "estado",
                    "cep",
                    "tipo_de_barbearia",
                    "horario_de_abertura",
                    "horario_de_fechamento",
                    "data_de_criacao",
                    "data_de_atualizacao",
                ]
            },
        ],
    ]

    autocomplete_fields = ["dono"]

    list_select_related = ["dono"]

    filter_horizontal = ["funcionarios"]

    search_fields = [
        "nome_da_barbearia",
        "cnpj",
    ]

    readonly_fields = [
        "dono",
        "data_de_criacao",
        "data_de_atualizacao",
    ]

    inlines = [
        AvaliacaoInline,
        BarbeiroInline,
        ContatoInline,
        FinanceiroInline,
        FuncionarioInline,
        PlanosDeFidelidadeInline,
        ServicoInline,
    ]

    change_actions = [
        'exportar_dados'
    ]

    # actions = [
    #     'ola'
    # ]

    changelist_actions = [
        "atualizar_todas_as_financas",
    ]

    def atualizar_todas_as_financas(self, request, obj):
        Financeiro().atualizar_todas_as_financas(obj)

    def exportar_dados(self, request, obj):
        from django.http import HttpResponse

        with transaction.atomic():
            barbearia = Barbearia.objects.get(id=obj.id)
            financeiro = barbearia.financeiro.__dict__
            
            for key in list(financeiro.keys()):
                if key in ["_state", "id", "comparar_lucros_mes_anterior_e_atual"]:
                    financeiro.pop(key)
                    print(f"Chave excluida: {key}")

            financeiro["barbearia_id"] = barbearia.nome_da_barbearia
            financeiro["lucro"] = "Sim" if financeiro["lucro"] is True else "Não"
            financeiro["prejuizo"] = "Sim" if financeiro["prejuizo"] is True else "Não"

            df = pd.DataFrame([financeiro])

            output = BytesIO()

            with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
                df.to_excel(writer, sheet_name="planilha", index=False)

            output.seek(0)

            response = HttpResponse(
                output.getvalue(),
                content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
            response["Content-Disposition"] = (
                f"attachment; filename={barbearia.nome_da_barbearia}.xlsx"
            )

            return response
        
    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if not request.user.is_superuser:
            queryset = queryset.filter(
                Q(dono=request.user) | Q(funcionarios=request.user)
            )

        return queryset


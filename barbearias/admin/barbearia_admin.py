from io import BytesIO
import xlsxwriter

import nested_admin
import pandas as pd
from admin_auto_filters.filters import AutocompleteFilter
from django.contrib import admin, messages
from django.db import transaction
from django.db.models import Q
from django_object_actions import DjangoObjectActions
from decimal import Decimal
from import_export.admin import ImportExportModelAdmin

from agendamentos.admin.servico_inline import ServicoInline

from ..models import Barbearia, Financeiro
from .avaliacao_inline import AvaliacaoInline
from .contato_inline import ContatoInline
from .financeiro_inline import FinanceiroInline
from .funcionario_inline import FuncionarioInline
from .plano_fidelidade_inline import PlanosDeFidelidadeInline


class DonoFilter(AutocompleteFilter):
    title = 'Dono'
    field_name = 'dono'


class FuncionarioFilter(AutocompleteFilter):
    title = 'Funcionário'
    field_name = 'funcionarios'


@admin.register(Barbearia)
class BarbeariaAdmin(DjangoObjectActions, nested_admin.NestedModelAdmin):
    list_display = [
        'nome_da_barbearia',
        'dono',
        'quantidade_de_agendamentos',
        'orcamento',
        'ultimo_agendamento',
        'numero_de_contatos',
        'avisos_recentes',
        'ultima_avaliacao',
        'media_das_avaliacoes',
    ]

    fieldsets = [
        [
            'Informações',
            {
                'fields': [
                    'nome_da_barbearia',
                    'dono',
                    'cnpj',
                    'funcionarios',
                    'rua',
                    'bairro',
                    'complemento',
                    'cidade',
                    'estado',
                    'cep',
                    'tipo_de_barbearia',
                    'media_das_avaliacoes',
                    'horario_de_abertura',
                    'horario_de_fechamento',
                    'data_de_criacao',
                    'data_de_atualizacao',
                ]
            },
        ],
    ]

    autocomplete_fields = ['dono']

    list_filter = [
        DonoFilter,
        FuncionarioFilter,
        'media_das_avaliacoes',
    ]

    list_select_related = ['dono']

    filter_horizontal = ['funcionarios']

    search_fields = [
        'nome_da_barbearia',
        'cnpj',
    ]

    readonly_fields = [
        'dono',
        'data_de_criacao',
        'data_de_atualizacao',
        'media_das_avaliacoes',
    ]

    inlines = [
        AvaliacaoInline,
        ContatoInline,
        FinanceiroInline,
        FuncionarioInline,
        PlanosDeFidelidadeInline,
        ServicoInline,
    ]

    change_actions = ['exportar_dados']

    # actions = [
    #     'ola'
    # ]

    changelist_actions = [
        'atualizar_todas_as_financas',
    ]

    def atualizar_todas_as_financas(self, request, obj):
        Financeiro().atualizar_todas_as_financas(obj)

    def exportar_dados(self, request, obj):
        from django.http import HttpResponse

        with transaction.atomic():
            output = BytesIO()
            workbook = xlsxwriter.Workbook(output)
            worksheet = workbook.add_worksheet()
            financeiro = obj.financeiro.__dict__

            for key in list(financeiro.keys()):
                if key in [
                    '_state',
                    'id',
                ]:
                    financeiro.pop(key)
                    print(f'Chave excluida: {key}')

            financeiro['barbearia_id'] = obj.nome_da_barbearia
            financeiro['lucro'] = (
                'Sim' if financeiro['lucro'] is True else 'Não'
            )
            financeiro['prejuizo'] = (
                'Sim' if financeiro['prejuizo'] is True else 'Não'
            )

            lucro_mes_anterior = Decimal(
                financeiro['lucro_mes_anterior']
            ).quantize(Decimal('0.0'))
            data = {
                'Barbearia': financeiro['barbearia_id'],
                'Receita total': f"R$ {financeiro['receita_total']}",
                'Lucro total': f"R$ {financeiro['lucro_total']}",
                'Despesas': f"R$ {financeiro['despesas']}",
                'Lucro planos': f"R$ {financeiro['lucro_planos']}",
                'Lucro mes anterior': f'R$ {lucro_mes_anterior}',
                'Lucros mes anterior/atual': f"R$ {financeiro['comparar_lucros_mes_anterior_e_atual']}",
                'Lucros mes anterior/atual porcentagem': f"%{financeiro['comparar_lucros_mes_anterior_e_atual_porcentagem']}",
                'Lucro': financeiro['lucro'],
                'Prejuizo': financeiro['prejuizo'],
            }

            df = pd.DataFrame([data])
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                df.to_excel(writer, sheet_name='planilha', index=False)
                worksheet = writer.sheets['planilha']

                worksheet.set_default_row(15)
                for column, value in enumerate(df.columns.values):
                    worksheet.set_column(column, column, 40)

            output.seek(0)

            response = HttpResponse(
                output.getvalue(),
                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            )
            response[
                'Content-Disposition'
            ] = f'attachment; filename={obj.nome_da_barbearia}.xlsx'

            return response

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if not request.user.is_superuser:
            queryset = queryset.filter(
                Q(dono=request.user) | Q(funcionarios=request.user)
            )

        return queryset

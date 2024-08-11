from io import BytesIO
import xlsxwriter

import nested_admin
import pandas as pd

from decimal import Decimal
from django.contrib import admin
from django.http import HttpResponse
from django.db import transaction
from django_object_actions import DjangoObjectActions
from admin_auto_filters.filters import AutocompleteFilter
from import_export.admin import ImportExportModelAdmin

from ..models import Financeiro


class BarbeariaFilter(AutocompleteFilter):
    title = 'Barbearia'
    field_name = 'barbearia'


@admin.register(Financeiro)
class FinanceiroAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = [
        'barbearia',
        'lucro_total',
        'receita_total',
        'despesas',
    ]

    fieldsets = [
        [
            'Financeiro',
            {
                'fields': [
                    'barbearia',
                    'lucro_total',
                    'receita_total',
                    'lucro_planos',
                    'lucro_produtos',
                    'despesas',
                ]
            },
        ],
        [
            'Lucros Mensais',
            {
                'fields': [
                    'lucro_mes_anterior',
                    'renda_mensal',
                    'comparar_lucros_mes_anterior_e_atual',
                    'comparar_lucros_mes_anterior_e_atual_porcentagem',
                    'prejuizo',
                    'lucro',
                ]
            },
        ],
    ]

    autocomplete_fields = [
        'barbearia',
    ]

    list_filter = [
        BarbeariaFilter,
    ]

    change_actions = [
        'atualizar_financas',
        'limpar_financeiro',
    ]

    changelist_actions = [
        'atualizar_todos_os_financeiros',
        'exportar_financeiros',
    ]

    def atualizar_todos_os_financeiros(self, request, obj):
        # Financeiro.atualizar_todas_as_financas(self, obj)
        Financeiro().atualizar_todas_as_financas(obj)

    def atualizar_financas(self, request, obj):
        Financeiro().atualizar_financas(obj)

    def limpar_financeiro(self, request, obj):
        Financeiro()._limpar_financeiro(obj)

    def exportar_financeiros(self, request, obj):
        with transaction.atomic():
            output = BytesIO()
            workbook = xlsxwriter.Workbook(output)
            worksheet = workbook.add_worksheet()
            data = []

            for instance in obj:
                lucro = 'Sim' if instance.lucro else 'Não'
                prejuizo = 'Sim' if instance.prejuizo else 'Não'
                lucro_mes_anterior = Decimal(
                    instance.lucro_mes_anterior
                ).quantize(Decimal('0.00'))
                data.append(
                    {
                        'barbearia': instance.barbearia,
                        'lucro_total': instance.lucro_total,
                        'receita_total': instance.receita_total,
                        'despesas': instance.despesas,
                        'lucro': lucro,
                        'prejuizo': prejuizo,
                        'lucro_mes_anterior': lucro_mes_anterior,
                        'renda_mensal': instance.renda_mensal,
                        'comparar_lucros_mes_anterior_e_atual': instance.comparar_lucros_mes_anterior_e_atual,
                        'comparar_lucros_mes_anterior_e_atual_porcentagem': instance.comparar_lucros_mes_anterior_e_atual_porcentagem,
                        'lucro_planos': instance.lucro_planos,
                        'lucro_produtos': instance.lucro_produtos or 0
                    }
                )

            df = pd.DataFrame(data)
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                df.to_excel(writer, sheet_name='planilha', index=False)
                worksheet = writer.sheets['planilha']

                # Ajusta a altura das linhas
                worksheet.set_default_row(15)

                # Ajusta a largura das colunas com base no tamanho dos dados
                for column, value in enumerate(df.columns):
                    max_length = max(
                        df[value].astype(str).map(len).max(), len(value)
                    )
                    worksheet.set_column(
                        column, column, max_length + 2
                    )  # Adiciona um buffer para espaçamento

            output.seek(0)

            response = HttpResponse(
                output.getvalue(),
                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            )
            response[
                'Content-Disposition'
            ] = f'attachment; filename=informacoes_dos_financeiros.xlsx'

            return response
        
    exportar_financeiros.label = 'Exportar todos os financeiros'

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

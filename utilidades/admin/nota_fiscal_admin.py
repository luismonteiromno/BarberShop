from decimal import Decimal

from admin_auto_filters.filters import AutocompleteFilter
from django.contrib import admin
from django_object_actions import DjangoObjectActions

from ..models import NotaFiscal


class ClienteFilter(AutocompleteFilter):
    title = 'Cliente'
    field_name = 'cliente'


@admin.register(NotaFiscal)
class NotaFiscalAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = [
        'id',
        'barbearia',
        'numero',
        'cliente',
        'status',
        'valor_unitario',
        'valor_total',
        'data_emissao',
    ]

    search_fields = ['numero', 'cliente__nome']

    autocomplete_fields = ['cliente', 'produto']

    list_filter = [
        ClienteFilter,
    ]

    changelist_actions = ['emitir_nfs']

    def emitir_nfs(self, request, objs):
        from io import BytesIO

        import pandas as pd
        import xlsxwriter
        from django.http import HttpResponse

        data = []
        for instance in objs:
            data.append(
                {
                    'Barbearia': instance.barbearia,
                    'Número': instance.numero,
                    'Cliente': instance.cliente.cliente,
                    'Status': instance.status,
                    'Valor Unitário': f' R$ {Decimal(instance.valor_unitario).quantize(Decimal("0.00"))}',
                    'Valor Total': f'R$ {Decimal(instance.valor_total).quantize(Decimal("0.00"))}',
                    'Data de emissão': instance.data_emissao.strftime('%d/%m/%Y'),
                }
            )

        output = BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet()
        df = pd.DataFrame(data)

        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, sheet_name='Notas Fiscais', index=False)
            worksheet = writer.sheets['Notas Fiscais']

            # Ajusta a altura das linhas
            worksheet.set_default_row(15)

            # Ajusta a largura das colunas com base no tamanho dos dados
            for column, value in enumerate(df.columns):
                max_length = max(
                    df[value].astype(str).map(len).max(), len(value)
                )
                worksheet.set_column(
                    column, column, max_length + 3
                )  # Adiciona um buffer para espaçamento

        output.seek(0)

        response = HttpResponse(
            output.getvalue(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        )
        response[
            'Content-Disposition'
        ] = f'attachment; filename=notas_fiscais.xlsx'

        return response

    emitir_nfs.label = 'Emitir planilha com as NFs'

    def has_add_permission(self, request, obj=None) -> bool:
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False

    def has_delete_permission(self, request, obj=None) -> bool:
        return False

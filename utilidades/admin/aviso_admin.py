from datetime import datetime

from django.contrib import admin, messages
from django_object_actions import DjangoObjectActions
from rangefilter.filters import (
    DateRangeFilterBuilder,
    DateTimeRangeFilterBuilder,
    NumericRangeFilterBuilder,
    DateRangeQuickSelectListFilterBuilder,
)

from modules import DadosDeMercado

from ..forms import AvisoForm
from ..models import Aviso


@admin.register(Aviso)
class AvisoAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = [
        'id',
        'barbearia',
        'data_de_inicio',
        'data_de_encerramento',
    ]

    autocomplete_fields = [
        'barbearia'
    ]
    
    list_filter = [
        ('data_de_inicio', DateRangeFilterBuilder()),
        ('data_de_encerramento', DateRangeFilterBuilder()),
    ]
    
    changelist_actions = [
        'remover_anuncios_passados',
    ]
    
    form = AvisoForm
    
    def remover_anuncios_passados(self, request, obj):
        for instance in obj:
            data_atual = datetime.strftime(datetime.now(), '%d/%m/%Y %H:%M:%S')
            data_marcada = datetime.strftime(instance.data_de_encerramento, '%d/%m/%Y %H:%M:%S')
            if data_atual >= data_marcada:
                instance.delete()
                self.message_user(request, 'Histórico de anúncio deletado com sucesso!')
    
    # def cotacoes(self, request, obj):
    #     print(DadosDeMercado().cotacoes('WEGE3'))
    #     print(DadosDeMercado().cotacoes('WEGE3', period_init='2024-06-01', period_end='2024-07-01'))
                
    # def dividendos(self, request, obj):
    #     print(DadosDeMercado().dividendos('WEGE3'))
    #     print(DadosDeMercado().dividendos('WEGE3', date_from='2024-06-01'))
        
    # def desdobramentos(self, request, obj):
    #     print(DadosDeMercado().desdobramentos('WEGE3'))
        
    # def lista_de_ativos(self, request, obj):
    #     print(DadosDeMercado().lista_de_ativos())
    #     print(DadosDeMercado().lista_de_ativos(tipo_do_ativo='stock'))
    #     print(DadosDeMercado().lista_de_ativos(tipo_do_ativo='reit'))

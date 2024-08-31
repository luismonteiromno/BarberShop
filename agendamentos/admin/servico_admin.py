from django.contrib import admin

from ..models import Servico
from django.utils.translation import gettext as _

from admin_auto_filters.filters import AutocompleteFilter, AutocompleteSelect
from global_functions.filter import SingleTextInputFilter

class BarbeariaFilter(AutocompleteFilter):
    title = 'Barbearia'
    field_name = 'disponivel_na_barbearia'

class CategoriaFilter(AutocompleteFilter):
    title = 'Categoria'
    field_name = 'categoria'
    
    # def queryset(self, request, obj):
    #     if self.value():
    #         return obj.filter(categoria__nome__icontains=self.value())
        
class NomeDoServicoFilter(SingleTextInputFilter):
    title = 'Nome do Serviço'
    parameter_name = 'nome_do_servico'
    
    def queryset(self, request, obj):
        if self.value():
            return obj.filter(nome_do_servico__icontains=self.value())

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = [
        'nome_do_servico', 
        'tempo_de_duracao_minutos', 
        'preco',
        'promocao_atual',
        'ultima_promocao'
    ]
    
    search_fields = [
        'nome_do_servico'
    ]
    
    autocomplete_fields = [
        'categoria',
        'disponivel_na_barbearia',
    ]
    
    list_filter = [
        BarbeariaFilter,
        CategoriaFilter,
        NomeDoServicoFilter,
    ]
    
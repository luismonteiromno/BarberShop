from django.contrib import admin
from ..models import Funcionario

from global_functions.filter import SingleTextInputFilter

from .filters import CargoFilter


class CPFBarbeiroFilter(SingleTextInputFilter):
    title = 'CPF do Barbeiro'
    parameter_name = 'cpf'

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(cpf__icontains=self.value())


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
        'cpf',
        'cargo',
    ]

    search_fields = [
        'nome',
        'cpf',
    ]

    autocomplete_fields = [
        'barbearia',
        'cargo',
    ]

    list_filter = [CargoFilter, CPFBarbeiroFilter]

    list_select_related = ['barbearia', 'cargo']

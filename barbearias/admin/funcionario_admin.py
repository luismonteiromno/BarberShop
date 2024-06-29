from django.contrib import admin
from ..models import Funcionario


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
        'cpf',
        'cargo',
    ]
    
    autocomplete_fields = [
        'cargo',
    ]
    
    list_select_related = ['cargo']
from django.contrib import admin
from ..models import Agendamento

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = [
        'usuario',
        'data_marcada',
    ]
    
    autocomplete_fields = [
        'escolher_barbeiro',
    ]
    
    filter_horizontal = [
        'servico'
    ]
    
    readonly_fields = [
        'usuario',
        'preco_do_servico'
    ]

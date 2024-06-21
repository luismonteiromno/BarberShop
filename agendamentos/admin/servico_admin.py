from datetime import datetime

from django.contrib import admin

from ..models import Servico


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = [
        'nome_do_servico', 
        'tempo_de_duracao', 
        'preco',
        'promocao_atual',
        'ultima_promocao'
    ]
    
    search_fields = [
        'nome_do_servico'
    ]
    
    autocomplete_fields = [
        'categoria',
        'disponivel_na_barbearia'
    ]
    
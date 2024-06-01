from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from datetime import datetime
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
        'disponivel_na_barbearia'
    ]
    
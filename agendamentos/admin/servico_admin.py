from django.contrib import admin

from ..models import Servico


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = [
        'nome_do_servico', 
        'tempo_de_duracao', 
        'preco'
    ]
    
    search_fields = [
        'nome_do_servico'
    ]
    
    autocomplete_fields = [
        'disponivel_na_barbearia'
    ]
    
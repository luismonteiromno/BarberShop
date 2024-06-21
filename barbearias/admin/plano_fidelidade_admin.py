from django.contrib import admin

from ..models import PlanosDeFidelidade
from .cliente_inline import ClienteInline


@admin.register(PlanosDeFidelidade)
class PlanosDeFidelidadeAdmin(admin.ModelAdmin):
    list_display = [
        'barbearia',
        'nome',
        'preco',
    ]
    
    search_fields = [
        'nome'
        'barbearia__nome_da_barbearia'
    ]
    
    exclude = [
        'quantidade_de_cortes'
    ]
    
    autocomplete_fields = [
        'barbearia'
    ]
    
    readonly_fields = [
        'usuarios'
    ]
    
    inlines = [
        ClienteInline,
    ]
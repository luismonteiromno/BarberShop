from django.contrib import admin
from ..models import PlanosDeFidelidade

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
    
    autocomplete_fields = [
        'barbearia'
    ]
    
    readonly_fields = [
        'usuarios'
    ]
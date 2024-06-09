from django.contrib import admin
from ..models import PlanosDeFidelidade

class PlanosDeFidelidadeInline(admin.TabularInline):
    model = PlanosDeFidelidade
    extra = 0
    
    fields = [
        'nome',
        'beneficios',
        'preco',
        'usuarios',
    ]
    
    readonly_fields = [
        'usuarios'
    ]
    
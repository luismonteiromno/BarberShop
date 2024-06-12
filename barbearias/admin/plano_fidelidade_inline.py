from django.contrib import admin
import nested_admin
from ..models import PlanosDeFidelidade
from .cliente_inline import ClienteInline

class PlanosDeFidelidadeInline(nested_admin.NestedTabularInline):
    model = PlanosDeFidelidade
    extra = 0
    
    inlines = [
        ClienteInline,
    ]
    
    fields = [
        'nome',
        'beneficios',
        'preco',
        'usuarios',
    ]
    
    readonly_fields = [
        'usuarios'
    ]
    
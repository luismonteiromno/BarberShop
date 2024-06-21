import nested_admin
from django.contrib import admin

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
    
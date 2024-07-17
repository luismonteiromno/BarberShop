import nested_admin

from ..models import ChavePix


class ChavePixInline(nested_admin.NestedTabularInline):
    model = ChavePix
    extra = 1
    readonly_fields = [
        'chave_aleatoria',
        'data_de_criacao',
        'data_de_atualizacao',
    ]
    
    def has_change_permission(self, request, obj=None):
        return False
            
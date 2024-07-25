import nested_admin

from ..forms import ChavePixForm
from ..models import ChavePix


class ChavePixInline(nested_admin.NestedTabularInline):
    model = ChavePix
    extra = 0
    readonly_fields = [
        'chave_aleatoria',
        'data_de_criacao',
        'data_de_atualizacao',
    ]
    
    form = ChavePixForm
    
    def has_change_permission(self, request, obj=None):
        return False
            
import nested_admin
from ..models import Cartao


class CartaoInline(nested_admin.NestedTabularInline):
    model = Cartao
    extra = 1
    
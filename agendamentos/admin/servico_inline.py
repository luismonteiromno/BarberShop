import nested_admin
from django.contrib import admin

from ..models import Servico


class ServicoInline(nested_admin.NestedStackedInline):
    model = Servico
    extra = 0
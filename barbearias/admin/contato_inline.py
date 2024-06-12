import nested_admin
from django.contrib import admin

from ..models import Contato


class ContatoInline(nested_admin.NestedStackedInline):
    model = Contato
    extra = 0
    
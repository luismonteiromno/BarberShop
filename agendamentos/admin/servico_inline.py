from django.contrib import admin

from ..models import Servico

class ServicoInline(admin.StackedInline):
    model = Servico
    extra = 0
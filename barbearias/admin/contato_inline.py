from django.contrib import admin
from ..models import Contato

class ContatoInline(admin.StackedInline):
    model = Contato
    extra = 0
    
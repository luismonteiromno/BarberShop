from django.contrib import admin

from ..models import Avaliacao


class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 0
    
    autocomplete_fields = [
        'usuario'
    ]
    
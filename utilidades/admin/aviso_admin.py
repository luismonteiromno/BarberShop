from django.contrib import admin
from ..models import Aviso

@admin.register(Aviso)
class AvisoAdmin(admin.ModelAdmin):
    list_display = [
        'barbearia',
        'data_de_inicio',
        'data_de_encerramento',
    ]

    autocomplete_fields = [
        'barbearia'
    ]

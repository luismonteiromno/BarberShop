from django.contrib import admin
from ..models import AvaliacaoDoBarbeiro

@admin.register(AvaliacaoDoBarbeiro)
class AvaliacaoDoBarbeiroAdmin(admin.ModelAdmin):
    list_display = [
        'barbeiro',
        'avaliacao',
    ]
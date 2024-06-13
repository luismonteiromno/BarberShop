from django.contrib import admin

from ..models import Promocao


@admin.register(Promocao)
class PromocaoAdmin(admin.ModelAdmin):
    list_display = [
        'servico',
        'nome_da_promocao',
        'inicio_da_promocao',
        'fim_da_promocao',
    ]
    
    autocomplete_fields = [
        'servico',
        'plano_fidelidade',
    ]
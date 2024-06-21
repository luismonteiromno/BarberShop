from django.contrib import admin

from ..models import CategoriaDoServico


@admin.register(CategoriaDoServico)
class CategoriaDoServicoAdmin(admin.ModelAdmin):
    list_display = [
        'nome'
    ]
    
    search_fields = [
        'nome'
    ]
from django.contrib import admin
from ..models import Cargo


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = [
        'nome_do_cargo',
        'nivel_hierarquico',
    ]
    
    search_fields = [
        'nome_do_cargo',
        'nivel_hierarquico',
    ]
    
    list_filter = [
        'nivel_hierarquico',
    ]
    
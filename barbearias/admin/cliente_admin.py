from django.contrib import admin
from ..models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = [
        'cliente',
        'plano_de_fidelidade',
    ]
    
    autocomplete_fields = [
        'cliente',
        'plano_de_fidelidade',
    ]
    
    list_select_related = True
    
    
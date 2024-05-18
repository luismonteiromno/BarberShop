from django.contrib import admin
from django_object_actions import DjangoObjectActions

from ..models import Aviso

@admin.register(Aviso)
class AvisoAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = [
        'id',
        'barbearia',
        'data_de_inicio',
        'data_de_encerramento',
    ]

    autocomplete_fields = [
        'barbearia'
    ]
    
    changelist_actions = [
        
    ]
    
    def remover_anuncios(self, request, obj):
        for instance in obj:
            instance.delete()

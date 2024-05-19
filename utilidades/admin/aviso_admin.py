from django.contrib import admin
from django_object_actions import DjangoObjectActions

from ..models import Aviso
from ..forms import AvisoForm

from datetime import datetime

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
        'remover_anuncios'
    ]
    
    form = AvisoForm
    
    def remover_anuncios(self, request, obj):
        for instance in obj:
            data_atual = datetime.strftime(datetime.now(), '%d/%m/%Y %H:%M:%S')
            data_marcada = datetime.strftime(instance.data_de_encerramento, '%d/%m/%Y %H:%M:%S')
            if data_atual >= data_marcada:
                instance.delete()
                self.message_user(request, 'Histórico de anúncio deletado com sucesso!')

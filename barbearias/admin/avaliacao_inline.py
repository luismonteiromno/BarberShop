from django.contrib import admin
from django.http import HttpRequest

from ..models import Avaliacao


class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 0
    max_num = 0
    can_delete = False
    
    autocomplete_fields = [
        'usuario'
    ]
    
    def has_change_permission(self, request, obj):
        return False
    
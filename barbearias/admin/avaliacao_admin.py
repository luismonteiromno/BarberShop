from django.contrib import admin
from django.http import HttpRequest 
from ..models import Avaliacao

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = [
        'avaliacao',
        'barbearia',
        'usuario',
    ]
    
    def has_add_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
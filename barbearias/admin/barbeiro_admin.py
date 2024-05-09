from typing import Any
from django.contrib import admin
from django.contrib.auth.models import User
from ..models import Barbeiro

@admin.register(Barbeiro)
class BarbeiroAdmin(admin.ModelAdmin):
    list_display = [
        'barbeiro',
        'barbearia',
    ]
    
    autocomplete_fields = [
        'barbearia',
        'servicos'
    ]
    
    search_fields = [
        'nome_do_barbeiro',
        'barbearia__nome_da_barbearia',
    ]
    
    list_select_related = [
        'barbearia',
    ]
    
    list_filter = [
        'barbearia',
    ]
    
    def formfield_for_foreignkey(self, db_field, request,**kwargs):
        if db_field.name == 'barbeiro':
            kwargs['queryset'] = User.objects.filter(profile__tipo_do_usuario='Barbeiro')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
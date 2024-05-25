from typing import Any

import django.db.models
from django.contrib import admin
from django.contrib.auth.models import User

from ..models import Barbeiro


@admin.register(Barbeiro)
class BarbeiroAdmin(admin.ModelAdmin):
    list_display = [
        'barbeiro',
        'barbearia',
        'freelancer'
    ]
    
    fieldsets = [
        ['informações', {
            'fields': [
                'barbeiro', 
                'barbearia', 
                'servicos', 
                'freelancer'
            ]
        }]
    ]
    
    autocomplete_fields = [
        'barbearia',
    ]
    
    search_fields = [
        'nome_do_barbeiro',
        'barbearia__nome_da_barbearia',
    ]
    
    filter_horizontal = [
        'servicos'
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
    
    def get_queryset(self, request):
        queryset =  super().get_queryset(request)
        
        if not request.user.is_superuser:
            queryset = queryset.filter(
                barbearia__dono=request.user
            ).select_related('barbearia__dono')
            
        return queryset
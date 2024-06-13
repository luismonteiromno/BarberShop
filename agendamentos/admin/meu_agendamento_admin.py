from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from ..models import MeuAgendamento

@admin.register(MeuAgendamento)
class MeuAgendamentoAdmin(admin.ModelAdmin): 
    list_display = [
        'agendamento',
        'cliente',
    ]
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        
        if not request.user.is_superuser:
            queryset = queryset.filter(cliente=request.user)
            
        return queryset
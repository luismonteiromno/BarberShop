from django.contrib import admin
from ..models import Agendamento


from django.contrib.auth.models import User

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = [
        'usuario',
        'servico',
        'data_marcada',
    ]
    
    autocomplete_fields = [
        'servico'
    ]
    
    readonly_fields = [
        'usuario',
        'preco_do_servico'
    ]
    
    def formfield_for_foreignkey(self, db_field, request,**kwargs):
        if db_field.name == 'escolher_barbeiro':
            kwargs['queryset'] = User.objects.filter(profile__tipo_do_usuario='Barbeiro')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

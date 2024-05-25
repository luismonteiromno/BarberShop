
from django.contrib import admin
from django.contrib.auth.models import User

from ..models import Barbeiro


class BarbeiroInline(admin.TabularInline):
    model = Barbeiro
    extra = 0
    max_num = 1
    
    readonly_fields = [
        'barbeiro',
        'servicos'
    ]

    # def formfield_for_foreignkey(self, db_field, request,**kwargs):
    #     if db_field.name == 'barbeiro':
    #         kwargs['queryset'] = User.objects.filter(profile__tipo_do_usuario='Barbeiro')
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)


from django.contrib import admin
from django.contrib.auth.models import User

from ..models import Barbeiro

from admin_auto_filters.filters import AutocompleteFilter

class BarbeariaFilter(AutocompleteFilter):
    title = 'Barbearia'
    field_name = 'barbearia'

class ServicoFilter(AutocompleteFilter):
    title = 'Barbeiro'
    field_name = 'barbeiro'

@admin.register(Barbeiro)
class BarbeiroAdmin(admin.ModelAdmin):
    list_display = [
        'barbeiro',
        'avaliacao',
        'salario',
        'freelancer',
    ]

    fieldsets = [
        [
            'informações',
            {
                'fields': [
                    'barbeiro',
                    'barbearia',
                    'servicos',
                    'salario',
                    'avaliacao',
                    'freelancer',
                ]
            },
        ]
    ]

    autocomplete_fields = ['barbearias', 'servicos']

    search_fields = [
        'nome_do_barbeiro',
        'barbearias__nome_da_barbearia',
    ]

    list_select_related = True

    list_filter = [
        # 'barbearia',
        'salario',
        ServicoFilter,
        BarbeariaFilter,
    ]

    readonly_fields = [
        'avaliacao',
    ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'barbeiro':
            kwargs['queryset'] = User.objects.filter(
                profile__tipo_do_usuario='Barbeiro'
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if not request.user.is_superuser:
            queryset = queryset.filter(
                barbearia__dono=request.user
            ).select_related('barbearia__dono')

        return queryset

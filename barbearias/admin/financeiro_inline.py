import nested_admin
from django.contrib import admin

from ..models import Financeiro


class FinanceiroInline(nested_admin.NestedTabularInline):
    model = Financeiro
    extra = 0
    max_num = 0
    can_delete = False
    
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
    
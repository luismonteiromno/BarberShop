import nested_admin
from django.contrib import admin

from ..models import Cliente


class ClienteInline(nested_admin.NestedTabularInline):
    model = Cliente
    extra = 0
    can_delete = False
    
    def has_add_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
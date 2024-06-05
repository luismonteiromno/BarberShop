from django.http import HttpRequest
from ..models import Financeiro
from django.contrib import admin

class FinanceiroInline(admin.TabularInline):
    model = Financeiro
    extra = 0
    max_num = 0
    can_delete = False

    def has_change_permission(self, request, obj=None):
        return False
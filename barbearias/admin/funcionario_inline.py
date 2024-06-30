from django.contrib import admin
import nested_admin

from ..models import Funcionario

class FuncionarioInline(nested_admin.NestedStackedInline):
    model = Funcionario
    extra = 0
    
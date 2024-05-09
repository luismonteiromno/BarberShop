from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .usuario_admin import ProfileInline

admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    def get_list_display(self, request):
        list_display = super().get_list_display(request)
        id = ("id",)
        return id + list_display

    inlines = [
        ProfileInline,
    ]
    
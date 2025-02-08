from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'is_staff')
    search_fields = ('email', 'username')


admin.site.register(CustomUser, CustomUserAdmin)
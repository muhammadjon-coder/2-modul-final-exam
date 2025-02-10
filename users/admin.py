from django.contrib import admin
<<<<<<< HEAD
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'is_staff')
    search_fields = ('email', 'username')


admin.site.register(CustomUser, CustomUserAdmin)
=======

# Register your models here.
>>>>>>> 9727532 (Hatola hali kop)

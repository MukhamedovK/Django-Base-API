from django.contrib import admin

from .models import User


@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname', 'email', 'is_staff']
    save_on_top = True
    save_as = True

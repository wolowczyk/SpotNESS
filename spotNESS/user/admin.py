from django.contrib import admin
from user.models import SpotUser


@admin.register(SpotUser)
class SpotUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'localization']

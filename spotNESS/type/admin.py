from django.contrib import admin
from type.models import SpotType


@admin.register(SpotType)
class SpotTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']

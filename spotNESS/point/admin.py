from django.contrib import admin
from point.models import Point


@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'type', 'added']
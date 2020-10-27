from django.contrib import admin
from .models import Prevision, Futuro


class PrevisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


class FuturoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


admin.site.register(Prevision, PrevisionAdmin)
admin.site.register(Futuro, FuturoAdmin)

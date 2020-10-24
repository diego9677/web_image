from django.contrib import admin
from .models import Prevision, Futuro


class PrevisionAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'show')


class FuturoAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'show')


admin.site.register(Prevision, PrevisionAdmin)
admin.site.register(Futuro, FuturoAdmin)

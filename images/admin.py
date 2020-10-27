from django.contrib import admin
from .models import Prevision, Futuro
from django.urls import reverse
from django.template.defaultfilters import slugify


@admin.register(Prevision)
class PrevisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'full_url')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')

    def __init__(self, model, admin_site):
        self.request = None
        super().__init__(model, admin_site)

    def get_queryset(self, request):
        self.request = request
        return super(PrevisionAdmin, self).get_queryset(request)

    def full_url(self, obj: Prevision):
        return f'{self.request.build_absolute_uri(reverse("prevision-detail", args=[obj.id, slugify(obj.name)]))}'

    full_url.short_description = 'url generada'


@admin.register(Futuro)
class FuturoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'full_url')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')

    def full_url(self, obj: Futuro):
        return f'{self.request.build_absolute_uri(reverse("prevision-detail", args=[obj.id, slugify(obj.name)]))}'

    full_url.short_description = 'url generada'

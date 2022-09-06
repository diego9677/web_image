from django.contrib import admin
from .models import Prevision, Futuro
from django.urls import reverse
from django.template.defaultfilters import slugify
import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

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
        return super().get_queryset(request)

    def full_url(self, obj: Prevision):
        return f'http://{hostname}{reverse("prevision-detail", args=[obj.id, slugify(obj.name)])}'

    full_url.short_description = 'url generada'


@admin.register(Futuro)
class FuturoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'full_url')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')

    def __init__(self, model, admin_site):
        self.request = None
        super().__init__(model, admin_site)

    def get_queryset(self, request):
        self.request = request
        return super().get_queryset(request)

    def full_url(self, obj: Futuro):
        return f'http://{hostname}{reverse("futuro-detail", args=[obj.id, slugify(obj.name)])}'

    full_url.short_description = 'url generada'

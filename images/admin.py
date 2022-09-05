from django.contrib import admin
from .models import Prevision, Futuro
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.conf import settings
import socket

ip_address = socket.gethostbyname(socket.gethostname())

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
        return f'http://{ip_address}{reverse("prevision-detail", args=[obj.id, slugify(obj.name)])}'

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
        return f'http://{ip_address}{reverse("futuro-detail", args=[obj.id, slugify(obj.name)])}'

    full_url.short_description = 'url generada'

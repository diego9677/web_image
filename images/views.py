from django.views import generic
from .models import Prevision, Futuro


class PrevisionView(generic.DetailView):
    model = Prevision


class FuturoView(generic.DetailView):
    model = Futuro

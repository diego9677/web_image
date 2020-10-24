from django.shortcuts import render, redirect, reverse
from .models import Prevision, Futuro


def index(request):
    return redirect(reverse('prevision'))


def prevision(request):
    image = Prevision.objects.filter(show=True).order_by('id')
    context = {'image': None}
    if len(image) > 0:
        context = {'image': image[0]}
    return render(request, 'images/prevision.html', context)


def futuro(request):
    image = Futuro.objects.filter(show=True).order_by('id')
    context = {'image': None}
    if len(image) > 0:
        context = {'image': image[0]}
    return render(request, 'images/futuro.html', context)

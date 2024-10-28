from django.shortcuts import render
from .models import *


def bosh_sahifa(request):
    return render(request, 'bosh_sahifa.html')


def fakultet_haqida(request):
    return render(request, 'fakultet_haqida.html')



def kurslar(request):
    return render(request, 'kurslar.html')


def yangiliklar(request):
    return render(request, 'yangiliklar.html', )


def boglanish(request):
    return render(request, 'boglanish.html')


def kafedralar(request):
    return render(request, 'kafedralar.html', )

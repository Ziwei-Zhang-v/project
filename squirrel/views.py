from django.shortcuts import render

from .models import SquirrelDetail


def index(request):
    sightings = SquirrelDetail.objects.all()
    context = {
        'sightings': sightings,
    }
    return render(request, 'squirrel/index.html', context)

def sightings(request):
    sightings = SquirrelDetail.objects.all()
    context = {
        'sightings': sightings,
    }
    return render(request, 'squirrel/sightings.html', context)



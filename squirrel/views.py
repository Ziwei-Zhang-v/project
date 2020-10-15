from django.shortcuts import render

from .models import SquirrelDetail


def index(request):
    return render(request, 'squirrel/index.html', {})

def sightings(request):
    squirrel_details = SquirrelDetail.objects.all()
    context = {
        'squirrel_details': squirrel_details,
    }
    return render(request, 'squirrel/sightings.html', context)



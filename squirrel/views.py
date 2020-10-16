from django.shortcuts import render,redirect,get_object_or_404
from .models import SquirrelDetail
from django.http import HttpResponse
import json
import random
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from .forms import Form


def homepage(request):
    return render(request,'squirrel/homepage.html')

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


def squirrel_detail(request,unique_squirrel_id):
    squirrel = SquirrelDetail.objects.get(id = unique_squirrel_id)
    return HttpResponse(f"Hello,I'm {squirrel.unique_squirrel_id}")

def add(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/sightings/')
    else:
        form = Form()
        context = {'form':form,}
        return render(request,'squirrel/addnew.html',context)

def update(request,squirrel_id):
    Object = get_object_or_404(SquirrelDetail,unique_squirrel_id=squirrel_id)
    form = Form(request.POST or None, instance = Object)
    context = {'form':form}
    if form.is_valid():
        Object=form.save(commit=False)
        Object.save()
        return redirect('/sightings/')
    else:
        context={
                'form':form,
        }
        return render(request,'squirrel/update.html',context)

def stats(request):
    num_of_sightings = SquirrelDetail.objects.all().count()
    adult_age = SquirrelDetail.objects.filter(age='Adult').count()
    fur_cinnamon = SquirrelDetail.objects.filter(primary_fur_color='Cinnamon').count()
    fur_gray = SquirrelDetail.objects.filter(primary_fur_color='Gray').count()
    ground_plane_location = SquirrelDetail.objects.filter(location='Ground Plane').count()
    context = {
            'num_of_sightings':num_of_sightings,
            'adult_age':adult_age,
            'fur_cinnamon':fur_cinnamon,
            'fur_gray':fur_gray,
            'ground_plane_location':ground_plane_location,
            }
    return render(request,'squirrel/stats.html',context)

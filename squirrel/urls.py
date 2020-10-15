from django.urls import path

from . import views

App_name = 'squirrel'


urlpatterns = [
    path('', views.sightings, name='sightings'),
]

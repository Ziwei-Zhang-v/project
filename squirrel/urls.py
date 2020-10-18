from django.urls import path

from . import views
from django.conf.urls import url

App_name = 'squirrel'


urlpatterns = [
    path('', views.homepage),
    path('sightings/', views.sightings, name='sightings'),
    path('map/', views.index, name='index'),
    path('sightings/add/', views.add, name='add'),
    path('sightings/stats/', views.stats, name='stats'),
    path('sightings/<unique_squirrel_id>/', views.update, name='update'),
]

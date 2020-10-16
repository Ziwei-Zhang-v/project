from django.urls import path

from . import views

App_name = 'squirrel'


urlpatterns = [
    path('', views.homepage),
    path('sightings/', views.sightings, name='sightings'),
    path('map/', views.index,name='index'),
    path('sightings/add/', views.add,name='add'),
    path('sightings/<unique-squirrel-id>/', views.update,name='update'),
    path('sightings/stats/', views.stats,name='stats'),
]

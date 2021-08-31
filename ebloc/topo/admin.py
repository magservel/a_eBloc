from django.contrib import admin

# Register your models here.
from django.contrib.gis.admin import OSMGeoAdmin
from .models import *


@admin.register(Other)
class TopoAdmin(OSMGeoAdmin):
    list_display = ('name', 'type')


@admin.register(Sentier)
class TopoAdmin(OSMGeoAdmin):
    list_display = ('name', 'geom')


@admin.register(Sector)
class SectorAdmin(OSMGeoAdmin):
    list_display = ['name', 'geom']


@admin.register(Bloc)
class BlocAdmin(OSMGeoAdmin):
    list_display = ('name', 'sector')


@admin.register(Line)
class LineAdmin(OSMGeoAdmin):
    list_display = ['name']


@admin.register(Photo)
class PhotoAdmin(OSMGeoAdmin):
    list_display = ['photo']

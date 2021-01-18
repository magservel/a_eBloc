"""ebloc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from djgeojson.views import GeoJSONLayerView
from djgeojson.views import TiledGeoJSONLayerView
from topo import views
from topo.models import Line

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index),
    path('get/sectors', views.get_all_sectors, name='get_all_sectors'),
    path('get/others', views.get_all_others, name='get_all_others'),
    path('get/lines', views.get_all_lines, name='get_all_lines'),
    path('get/line', views.get_line, name='get_line'),
    path(r'^data.geojson$', GeoJSONLayerView.as_view(model=Line, properties=['name', 'calque', 'cota', 'printInfo']), name='lines', ),
]

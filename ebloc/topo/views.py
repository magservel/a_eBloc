from django.shortcuts import render
from django.views import generic
from djgeojson.serializers import Serializer as GeoJSONSerializer
from django.core.serializers import serialize
from django.template import loader

from django.http import HttpResponse, HttpResponseBadRequest

from .models import Sector, Other, Line


class Home(generic.ListView):
    model = Sector
    context_object_name = 'sectors'
    queryset = Sector.objects.all()
    template_name = 'index.html'


home = Home.as_view()


def index(request):
    lines = Line.objects.all()
    others = Other.objects.values()
    sectors = Sector.objects.values()

    print(lines[0].printInfo)
    context = {'lines': lines,
               'others': others,
               'sectors': sectors,
               }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request=request))


def get_all_sectors(request):
    if request.is_ajax():
        geojson_data = serialize('geojson', Sector.objects.all())
        return HttpResponse(geojson_data)
    msg = "Bad request: not AJAX"
    return HttpResponseBadRequest(msg)


def get_all_others(request):
    if request.is_ajax():
        geojson_data = serialize('geojson', Other.objects.all())
        return HttpResponse(geojson_data)
    msg = "Bad request: not AJAX"
    return HttpResponseBadRequest(msg)


def get_all_lines(request):
    if request.is_ajax():
        geojson_data = serialize('geojson', Line.objects.all())
        return HttpResponse(geojson_data)
    msg = "Bad request: not AJAX"
    return HttpResponseBadRequest(msg)


# TODO: finish this function
def get_line():
    pass
#     line = Line.objects.values().get(pk=1)
#     context = {'line': line}
#     template = loader.get_template('infos.html')
#     return HttpResponse(template.render(context))


from django.template import loader
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.core.serializers import serialize

from django.http import HttpResponse
from .models import Sector, Other, Line


def index(request):
    # sectors = serialize('geojson', Sector.objects.all())
    # lines = serialize('geojson', Line.objects.all())
    # others = serialize('geojson', Other.objects.all())
    context = {
        'sectors': serialize('geojson', Sector.objects.all()),
        'lines': serialize('geojson', Line.objects.all()),
        'others': serialize('geojson', Other.objects.all()),
    }
    template = loader.get_template('base.html')
    return HttpResponse(template.render(context, request=request))


class LineDetailView(generic.DetailView):
    model = Line

    def line_detail_view(request, primary_key):
        print(primary_key)
        line = get_object_or_404(Line, pk=primary_key)
        print(line)
        return render(request, 'line_detail.html', context={'line': line})

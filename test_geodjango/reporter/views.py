from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.core.serializers import serialize

from .models import Incident


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'reporter/index.html'


class DetailPageView(DetailView):
    model = Incident
    template_name = 'reporter/incident_detail.html'
    context_object_name = 'reporter'



def incidents_data(request):
    all_incidents_json = serialize('geojson', Incident.objects.all())
    return HttpResponse(all_incidents_json, content_type='json')

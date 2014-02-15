from django.shortcuts import render_to_response
from django.http import HttpResponse
from api import mapquest
import json


def index(request):
    data = mapquest.getIncidents()
    return render_to_response('index.html', {'data': mapquest.getIncidents(), 'json': json.dumps(data)})


def map(request):
    contents = mapquest.getMapImage(int(request.GET['w']) - 30, int(request.GET['h']) - 50)
    response = HttpResponse(contents, mimetype='image/gif')
    return response

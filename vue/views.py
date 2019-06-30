from django.shortcuts import render, HttpResponse
from . import fake_data
import json


def index(request):
    return render(request, 'vue/index.html')


def data(request):
    return HttpResponse(json.dumps(fake_data.stock_data), content_type="application/json")

import json

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .get_api_data import get_data

def index(request):
    return render(request,'website/index.html')

def details(request,detail_id):
    context = {
        'item': detail_id
    }
    return render(request,'website/details.html',context=context)

def salary(request):
    return render(request,'website/salary.html')

def analytics(request):
    l = get_data()
    context = {
        'l':l
    }
    return render(request,'website/analytics.html',context=context)

def v1_api(request):
    data = {
        'test_data':'test_data',
        'qwe':'qwe',
        'qqq':'www'
    }
    json_data = json.dumps(data)
    return HttpResponse(json_data,content_type="application/json")


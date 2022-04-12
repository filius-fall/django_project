import json
import requests

from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
# Create your views here.

from .models import Expenses,ExpDetails
from .get_api_data import get_data

def index(request):
    return render(request,'website/index.html')

def details(request,detail_id):
    context = {
        'item': detail_id
    }
    return render(request,'website/details.html',context=context)

def expenses(request):
    if request.method == 'POST':
        form = request.POST
        print(form)
        exp = Expenses(expense=int(form['expense']),date=timezone.now())
        exp.save()
        des = ExpDetails(expenses=exp,cause=form['des'],pub_data=timezone.now())
        des.save()
    return render(request,'website/expenses.html')

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


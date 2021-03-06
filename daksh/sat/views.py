import json
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404,render
from .api_data import daily_data

def index(request):
    data = daily_data()
    context = {'values':data,'test':1234555}
    return render(request,'sat/index.html',context=context)

def test(request):
    data = daily_data()
    tes = 1234
    context = {'values':data,'test':tes}
    return render(request,'sat/test.html',context=context)


def sat_api(request):
    data = [
        ('01-01-2021',7135),
        ('02-02-2021',155),
        ('23-03-2021',345),
        ('04-04-2021',289),
        ('05-05-2021',190),
        ('06-06-2021',197),
        ('07-07-2021',213),
        ('08-08-2021',156),
        ('09-09-2021',129),
        ('10-10-2021',88),
        ('11-11-2021',176),
        ('11-11-2021',180),
        ('11-11-2021',200),
        ('11-11-2021',188),
        ('11-11-2021',176),
        ('11-11-2021',444),
        ('11-11-2021',145),
        ('11-11-2021',176),
        ('11-11-2021',176),
        ('11-11-2021',176),
        ('11-11-2021',176),
        ('11-11-2021',176),
        ('11-11-2021',176),
        ('11-11-2021',176),
        ('11-11-2021',176),
        ('11-11-2021',176),
        ('11-11-2021',176),
        ('11-11-2021',176),
        ('11-11-2021',176),
        ('11-11-2021',176),
        ('11-11-2021',176),
        ('11-11-2021',176),
        ('11-11-2021',176),
        ('11-11-2021',176),
        ('11-11-2021',176),
        ('11-11-2021',176),
        ('11-11-2021',176),
        ('11-11-2021',176),
        ('11-11-2021',176),
        ('11-11-2021',176),
        ('11-11-2021',176),
        ('11-11-2021',176),
    ]

    lables = [row[0] for row in data]
    values = [row[1] for row in data]

    context = {
        'lables':lables,
        'values':values,
    }
    return HttpResponse(json.dumps(context),content_type="application/json")


def lobby(request):
    return render(request,'sat/lobby.html')


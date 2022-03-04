from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404,render

from .models import Questions,Choice

def index(request):
    get_question_list = Questions.objects.order_by('-pub_date')[:5]
    context = {'get_question_list': get_question_list}
    return render(request, 'polls/index.html',context=context)

def detail(request,question_id):
    choice_list = Choice.objects.get(pk=question_id)
    context = {'choice_list':choice_list}
    return render(request, 'polls/details.html',context=context)
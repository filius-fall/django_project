from django.shortcuts import render
from django.http import HttpResponse

from .db_actions import set_values, get_values, get_all_keys
from .forms import ExpensesForm
from .consumers import ChatConsumer

import json
# Create your views here.
def index(request):
    print('INISDE INDEX')
    print(request.method)
    form = ExpensesForm()
    if request.method == 'POST':
        form = ExpensesForm(request.POST)
        if form.is_valid():
            print('FORM IS VALID')
            data = form.cleaned_data
            print(data)
            print('AFTER SENDING MESSAGE')
            return HttpResponse(json.dumps({'status':'success'}), content_type='application/json')
    return render(request,'chat/index.html',{'form':form})

def room(request,room_name):
    return render(request,'chat/room.html',{'room_name':room_name})

def api(request):
    fake_data = {
        'name':'test',
        'message':'test message'
    }
    db_data = get_all_keys()
    print(db_data)
    return HttpResponse(json.dumps(fake_data), content_type='application/json')

def push_data_to_redis(request):
    print('INISDE PUSH DATA TO REDIS')
    print(request.method)
    if request.method == 'POST':
        data = request.POST
        print(data)
        set_values(data['name'],data['message'])
        return HttpResponse(json.dumps({'status':'success'}), content_type='application/json')


def message_from_consumer():
    k = ChatConsumer()
    k.send_message({'message':'test message for test from consumer'})

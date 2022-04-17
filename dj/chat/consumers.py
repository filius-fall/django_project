import json
import redis
from datetime import datetime
from channels.generic.websocket import WebsocketConsumer

from .db_actions import set_values, get_values, get_all_keys,hset_values,hgetall_values

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        print('CONNECTED')
        data = hgetall_values()
        d = sorted(data, key=lambda i: i['date'])
        print(d)
        self.send(text_data=json.dumps(d))
        

    def disconnect(self,close_code):
        pass
    
    def receive(self,text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        d = sorted(message, key=lambda i: i['date'])
        print("SETting VLAUES")
        hset_values(message)
        print("TEXT_DATA PRINTEDDDDDDDDDDDDDDDDDDDD",d)
        self.send(text_data=json.dumps({
            'message':d
        }))

    def send_message(self,event):
        message = event['message']
        self.send(text_data=json.dumps({
            'message':message
        }))
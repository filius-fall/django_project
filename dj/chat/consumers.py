import json
import redis
from channels.generic.websocket import WebsocketConsumer

from .db_actions import set_values, get_values, get_all_keys,hset_values,hgetall_values

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        print('CONNECTED')
        data = hgetall_values()
        print(data)
        

    def disconnect(self,close_code):
        pass
    
    def receive(self,text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print("SETting VLAUES")
        hset_values(message)
        print("TEXT_DATA PRINTEDDDDDDDDDDDDDDDDDDDD",message)
        self.send(text_data=json.dumps({
            'message':message
        }))

    def send_message(self,event):
        message = event['message']
        self.send(text_data=json.dumps({
            'message':message
        }))
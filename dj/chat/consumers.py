import json
import redis
from channels.generic.websocket import WebsocketConsumer

from .db_actions import set_values, get_values, get_all_keys

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        print('CONNECTED')
        print(get_all_keys())
        print('AFTER SENDING MESSAGE')
        main_dict = {}
        for i in get_all_keys():
            print('SENDING DATAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAas')
            data = get_values(i).decode('utf-8')
            print(data)
            i = i.decode('utf-8')
            main_dict[i] = data
        self.send(text_data=json.dumps({
                'message':main_dict
            }))    
        print("Main DICT IS EQUAL TO:",main_dict)

    def disconnect(self,close_code):
        pass
    
    def receive(self,text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print("TEXT_DATA PRINTEDDDDDDDDDDDDDDDDDDDD",text_data)
        self.send(text_data=json.dumps({
            'message':message
        }))

    def send_message(self,event):
        message = event['message']
        self.send(text_data=json.dumps({
            'message':message
        }))
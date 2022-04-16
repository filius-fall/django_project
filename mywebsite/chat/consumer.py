import json
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        print('connecteddddddddddddddddddddddddddd')
        self.send(text_data=json.dumps({
            'message': 'Now you are connected',
            'type':'Connection_established'
        }))

    def receive(self, text_data=None):
        # Called with either text_data or bytes_data for each frame
        # You can call:
        print("RECIREVED")
        self.send(text_data="Hello world!")
        # Or, to send a binary frame:
        
        # Or add a custom WebSocket error code!
        self.close(code=4123)

    def message(self):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        
        print('MESSAGE:',message)

    def disconnect(self):
        print("DADADADADADADADAD diSCSONENEGTED")
import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connetc(self):
        self.accept()
        self.send(text_data=json.dumps({
            'type':'Coonection Established Message',
            'message': 'You are now connected'

        }))
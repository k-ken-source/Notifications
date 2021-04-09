from channels.generic.websocket import WebsocketConsumer
from time import sleep
import json

class Consumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        iterator = 1
        while True:
            
            self.send(json.dumps({'NotificationNumber':iterator}))
            iterator += 1
            print("itr",iterator)
            sleep(10)
    




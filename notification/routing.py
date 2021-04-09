from django.urls import re_path,path
from .consumer import Consumer

websockets_urlpattern = [
    path('ws/notifications/',Consumer.as_asgi())
]
    
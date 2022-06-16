from django.urls import re_path
from app.middlewares import login_exempt
from django.views.decorators.csrf import csrf_exempt

from . import consumers

websocket_urlpatterns = [
	re_path(r'ws/socket-server/', ((consumers.ChatConsumer.as_asgi())))
]


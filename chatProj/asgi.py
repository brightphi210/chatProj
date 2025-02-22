

import os
# imports
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatProj.settings')

django_asgi_app = get_asgi_application()

from chatApp import routing

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": URLRouter(
        routing.websocket_urlpatterns
    )   
})

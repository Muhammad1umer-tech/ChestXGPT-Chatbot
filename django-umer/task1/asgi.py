"""
ASGI config for task1 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from app1.consumers import ChatConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task1.settings')

application = get_asgi_application()

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter([
        path('ws/test/', ChatConsumer.as_asgi()),
    ])
})

from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index),
    path('room', views.room, name='room'),
    path('send', views.message_send),
    path('message_listener', views.message_listener),
]

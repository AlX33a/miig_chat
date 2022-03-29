from django.urls import path
from .views import *

urlpatterns = [
    path('room/', APIRoom.as_view()),
    path('chat/', APIChat.as_view()),
    path('users/', APIAddUserRoom.as_view()),
]
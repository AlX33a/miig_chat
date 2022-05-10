from django.urls import path
from .views import *

urlpatterns = [
    path('room/', APIDialogue.as_view(), name="room"),
    path('chat/', APIChatDialogue.as_view()),
    path('search/', APIUserSearch.as_view()),
]
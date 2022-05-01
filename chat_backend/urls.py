from django.urls import path
from .views import *

urlpatterns = [
    path('room/', APIDialogue.as_view()),
    path('chat/', APIChatDialogue.as_view()),
]
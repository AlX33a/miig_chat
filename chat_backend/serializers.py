from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Dialogue, ChatToDialogue


# Для APIDialogue
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class UserNameSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", )


class DialogueSerializers(serializers.ModelSerializer):
    creator, invited = UserNameSerializers(), UserNameSerializers()
    class Meta:
        model = Dialogue
        fields = ("id", "creator", "invited", "is_read", "date")


# Для APIChatDialogue
class ChatDialogueSerializers(serializers.ModelSerializer):
    user = UserNameSerializers()
    class Meta:
        model = ChatToDialogue
        fields = ("user", "message", "date")


class ChatPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = ChatToDialogue
        fields = ("dialogue", "message")

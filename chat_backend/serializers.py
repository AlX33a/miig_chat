from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Room, Chat


class UserSerializers(serializers.ModelSerializer):
    """Сериализация юзера"""
    # Для улучшения сериализации вывода данных creator
    class Meta:
        model = User  # Ссылка на модель БД
        fields = ("id", "username")  # Обработка


class RoomSerializers(serializers.ModelSerializer):
    """Сериализация комнат чата"""
    # Позволяет получать инфу из БД и отдавать в json формат
    creator = UserSerializers()
    invited = UserSerializers(many=True)
    class Meta:
        model = Room  # Ссылка на модель БД
        fields = ("id", "creator", "invited", "date")  # Обработка

class ChatSerializers(serializers.ModelSerializer):
    """Сериализация чата"""
    user = UserSerializers()
    class Meta:
        model = Chat
        fields = ("user", "text", "date")

class ChatPostSerializers(serializers.ModelSerializer):
    """Сериализация пост запроса чата"""
    class Meta:
        model = Chat
        fields = ("room", "text")
from django.db.models import Q
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Room, Chat
from .serializers import (RoomSerializers, ChatSerializers, ChatPostSerializers, UserSerializers)


class APIRoom(APIView):
    """Вывод данных комнаты, гет запрос"""
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request):
        rooms = Room.objects.filter(Q(creator=request.user) | Q(invited=request.user))
        serializer = RoomSerializers(rooms, many=True)
        fix_serializer = [serializer.data[0]]
        if len(serializer.data) != 1:
            fix_serializer += [serializer.data[i] for i in range(1, len(serializer.data)) if serializer.data[i - 1]["id"] != serializer.data[i]["id"]]
        return Response({
            "data": fix_serializer
        })

    def post(self, request):
        Room.objects.create(creator=request.user)
        return Response(status=201)

class APIChat(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    # permission_classes = [permissions.AllowAny, ]
    def get(self, request):
        room = request.GET.get("room")
        chat = Chat.objects.filter(room=room)
        serializer = ChatSerializers(chat, many=True)
        return Response({
            "data": serializer.data
        })

    def post(self, request):
        # room = request.data.get("room")
        chat = ChatPostSerializers(data=request.data)
        if chat.is_valid():
            chat.save(user=request.user)
            return Response(status=201)
        else:
            return Response(status=400)


class APIAddUserRoom(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializers(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        room = request.data.get("room")
        user = request.data.get("user")
        try:
            room = Room.objects.get(id=room)
            room.invited.add(user)
            room.save()
            return Response(status=201)
        except:
            return Response(status=400)





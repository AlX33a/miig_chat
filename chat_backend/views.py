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
        fix_serializer = []
        fix_serializer = [odict for odict in serializer.data if odict not in fix_serializer]

        id_rooms = [odict["id"] for odict in fix_serializer]
        last_messages = []
        for ids in id_rooms:
            chat = Chat.objects.filter(room=ids)
            chat_serializer = ChatSerializers(chat, many=True)

            if chat_serializer.data:
                var = chat_serializer.data[-1]
                var.pop("user")
                var["id"] = ids
                last_messages += [var]

        return Response({
            "data": fix_serializer,
            "messages": last_messages
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
        user = request.GET.get("user")
        users = User.objects.filter(username=user)
        serializer = UserSerializers(users, many=True)
        return Response({
            "data": serializer.data
        })

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





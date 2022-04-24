from django.db.models import Q
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Room, Chat
from .serializers import (RoomSerializers, ChatSerializers, ChatPostSerializers, UserSerializers, ChatSerializersFIX)


class APIRoom(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        rooms = Room.objects.filter(Q(creator=request.user) | Q(invited=request.user))
        serializer = RoomSerializers(rooms, many=True)
        fix_serializer = []
        for odict in serializer.data:
            if odict not in fix_serializer:
                creator = odict.pop("creator")
                invited = odict.pop("invited")
                date = odict.pop("date")
                if str(request.user) == creator["username"]:
                    odict["invited"] = invited[0]["username"]
                    fix_serializer += [odict]
                else:
                    odict["invited"] = creator["username"]
                    fix_serializer += [odict]

                chat = Chat.objects.filter(room=odict["id"])
                chat_serializer = ChatSerializersFIX(chat, many=True)
                if chat_serializer.data:
                    odict["text"] = chat_serializer.data[-1]["text"]
                    odict["date"] = chat_serializer.data[-1]["date"]
                else:
                    odict["text"] = "Нажми, чтобы начать диалог!"
                    odict["date"] = date

        return Response({
            "data": fix_serializer,
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


class APIAddUser(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request):
        user = request.data.get("user")
        if str(request.user) == user:
            return Response({
                "Самому себе написать нельзя."
            }, status=400)
        users = User.objects.filter(username=user)
        serializer = UserSerializers(users, many=True)
        if serializer.data:
            if not (Room.objects.filter(Q(creator=request.user) & Q(invited=serializer.data[0]["id"])) or
                    Room.objects.filter(Q(creator=serializer.data[0]["id"]) & Q(invited=request.user))):
                room = Room.objects.create(creator=request.user)
                room.invited.add(serializer.data[0]["id"])
                room.save()
                return Response(status=201)
            return Response({
                "Диалог уже создан."
            }, status=400)
        return Response({
            "Пользователь не найден."
        }, status=400)

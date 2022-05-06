from django.db.models import Q
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Dialogue, ChatToDialogue
from .serializers import (DialogueSerializers, UserSerializers, ChatDialogueSerializers,
                          ChatPostSerializers)


class APIDialogue(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    @staticmethod
    def get(request):
        dialogues = Dialogue.objects.filter(Q(creator=request.user) | Q(invited=request.user))
        dialogue_serializer = DialogueSerializers(dialogues, many=True).data

        for index_odict in range(len(dialogue_serializer)):

            creator = dialogue_serializer[index_odict].pop("creator")["username"]
            invited = dialogue_serializer[index_odict].pop("invited")["username"]
            date = dialogue_serializer[index_odict].pop("date")

            if str(request.user) == creator:
                dialogue_serializer[index_odict]["invited"] = invited
            else:
                dialogue_serializer[index_odict]["invited"] = creator

            chat = ChatToDialogue.objects.filter(dialogue=dialogue_serializer[index_odict]["id"])
            chat_serializer = ChatDialogueSerializers(chat, many=True).data
            message_sender = chat_serializer[-1].pop("user")["username"]

            if chat_serializer:
                mess = chat_serializer[-1]["message"]
                if len(mess) < 14:
                    dialogue_serializer[index_odict]["message"] = mess
                else:
                    dialogue_serializer[index_odict]["message"] = mess[:14] + "..."
                dialogue_serializer[index_odict]["date"] = chat_serializer[-1]["date"]
                dialogue_serializer[index_odict]["message_sender"] = message_sender
            else:
                dialogue_serializer[index_odict]["message"] = "Нажми, чтобы начать диалог!"
                dialogue_serializer[index_odict]["date"] = date
                dialogue_serializer[index_odict]["message_sender"] = ""

        return Response({"data": dialogue_serializer})

    @staticmethod
    def post(request):
        user = request.data.get("user")
        if str(request.user) == user:
            return Response({"data": "Самому себе написать нельзя."}, status=400)

        invited_user = User.objects.filter(username=user)
        invited_user_serializer = UserSerializers(invited_user, many=True).data

        if invited_user_serializer:
            if not (Dialogue.objects.filter(Q(creator=request.user) & Q(invited=invited_user_serializer[0]["id"])) or
                    Dialogue.objects.filter(Q(creator=invited_user_serializer[0]["id"]) & Q(invited=request.user))):
                Dialogue.objects.create(creator=request.user, invited=invited_user[0]).save()

                return Response(status=201)
            return Response({"data": "Диалог уже создан."}, status=400)
        return Response({"data": "Пользователь не найден."}, status=400)


class APIChatDialogue(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    # permission_classes = [permissions.AllowAny, ]

    @staticmethod
    def get(request):
        dialogue_id = request.GET.get("dialogue")

        chat_dialogue = ChatToDialogue.objects.filter(dialogue=dialogue_id)
        chat_dialogue_serializer = ChatDialogueSerializers(chat_dialogue, many=True).data

        dialogues = Dialogue.objects.filter(id=dialogue_id)
        dialogue_serializer = DialogueSerializers(dialogues, many=True).data
        if not (str(request.user) in dialogue_serializer[0]["creator"]['username'] or
                str(request.user) in dialogue_serializer[0]["invited"]['username']):
            return Response({"data": "Вы не состоите в диалоге."}, status=400)

        if str(request.user) != chat_dialogue_serializer[-1]["user"]["username"]:
            dialogues[0].is_read = True
            dialogues[0].save()

        for index_odict in range(len(chat_dialogue_serializer)):
            chat_dialogue_serializer[index_odict]["user"] = chat_dialogue_serializer[index_odict]["user"]["username"]

        return Response({"data": chat_dialogue_serializer})

    @staticmethod
    def post(request):
        chat = ChatPostSerializers(data=request.data)

        if chat.is_valid():
            dialogues = Dialogue.objects.filter(id=request.data.get("dialogue"))
            dialogue_serializer = DialogueSerializers(dialogues, many=True).data

            if str(request.user) in dialogue_serializer[0]["creator"]['username'] or \
                    str(request.user) in dialogue_serializer[0]["invited"]['username']:
                chat.save(user=request.user)
                return Response(status=201)
            return Response({"data": "Вы не состоите в диалоге."}, status=400)
        return Response({"data": "Длина сообщения не может превышать 500 символов."}, status=400)

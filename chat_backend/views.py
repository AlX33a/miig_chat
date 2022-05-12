from django.db.models import Q
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Dialogue, ChatToDialogue
from .serializers import (DialogueSerializers, ChatDialogueSerializers, ChatPostSerializers, UserNameSerializers)


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

            if chat_serializer:
                mess = chat_serializer[-1]["message"]
                if len(mess) < 14:
                    dialogue_serializer[index_odict]["message"] = mess
                else:
                    dialogue_serializer[index_odict]["message"] = mess[:14] + "..."
                dialogue_serializer[index_odict]["date"] = chat_serializer[-1]["date"]
                dialogue_serializer[index_odict]["message_sender"] = chat_serializer[-1]["user"]["username"]
            else:
                dialogue_serializer[index_odict]["message"] = "Начните диалог!"
                dialogue_serializer[index_odict]["date"] = date
                dialogue_serializer[index_odict]["message_sender"] = ""

        return Response({"data": dialogue_serializer})

    @staticmethod
    def post(request):
        user = request.data.get("user")

        if str(request.user) == user:
            return Response({"data": "Самому себе написать нельзя."}, status=400)

        invited_user = User.objects.filter(username=user)
        if invited_user:
            if not Dialogue.objects.filter(Q(creator=request.user) & Q(invited=invited_user[0]) | Q(creator=invited_user[0]) & Q(invited=request.user)):
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

        dialogues = Dialogue.objects.filter(Q(creator=request.user) & Q(id=dialogue_id) | Q(invited=request.user) & Q(id=dialogue_id))

        if chat_dialogue:
            if str(request.user) != chat_dialogue_serializer[-1]["user"]["username"] and bool(chat_dialogue[len(chat_dialogue) - 1].is_read) is False:
                for i in range(len(chat_dialogue)):
                    if bool(chat_dialogue[i].is_read) is False:
                        chat_dialogue[i].is_read = True
                        chat_dialogue[i].save()

        if dialogues:
            if str(request.user) != chat_dialogue_serializer[-1]["user"]["username"] and bool(dialogues[0].is_read) is False:
                dialogues[0].is_read = True
                dialogues[0].save()

            for index_odict in range(len(chat_dialogue_serializer)):
                chat_dialogue_serializer[index_odict]["user"] = chat_dialogue_serializer[index_odict]["user"]["username"]

            return Response({"data": chat_dialogue_serializer})
        return Response({"data": "Вы не состоите в диалоге."}, status=400)

    @staticmethod
    def post(request):
        chat = ChatPostSerializers(data=request.data)
        dialogue_id = request.data.get("dialogue")

        if chat.is_valid():
            dialogues = Dialogue.objects.filter(Q(creator=request.user) & Q(id=dialogue_id) | Q(invited=request.user) & Q(id=dialogue_id))

            if dialogues:
                chat.save(user=request.user)

                if bool(dialogues[0].is_read) is True:
                    dialogues[0].is_read = False
                    dialogues[0].save()

                return Response(status=201)
            return Response({"data": "Вы не состоите в диалоге."}, status=400)
        return Response({"data": "Длина сообщения не может превышать 500 символов."}, status=400)

class APIUserSearch(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    @staticmethod
    def get(request):
        scroll_number = int(request.GET.get("scroll"))

        search = User.objects.filter(username__icontains=request.GET.get("user")).exclude(username=request.user)
        search_serializers = UserNameSerializers(search, many=True).data

        if search:
            if len(search) < 6:
                return Response({"data": search_serializers}, status=201)

            scrolling_options = []
            five_options = []
            for odict in search_serializers:
                five_options += [odict]
                if len(five_options) == 5:
                    scrolling_options += [five_options]
                    five_options = []
            scrolling_options += [five_options]

            if scroll_number == 1:
                return Response({"quantity": len(scrolling_options), "data": scrolling_options[scroll_number - 1]}, status=201)
            return Response({"data": scrolling_options[scroll_number - 1]}, status=201)
        return Response({"data": [{"username": "Пользователь не найден."}]}, status=201)
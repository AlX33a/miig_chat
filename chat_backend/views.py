from datetime import datetime, timezone, timedelta

from django.db.models import Q
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Dialogue, ChatToDialogue, TrackingUser
from .serializers import (DialogueSerializers, ChatDialogueSerializers, ChatPostSerializers, UserNameSerializers)

def tracking_user(request):
    if not TrackingUser.objects.filter(user=request.user):
        TrackingUser.objects.create(user=request.user).save()
    else:
        TrackingUser.objects.filter(user=request.user)[0].save()

class APIDialogue(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    @staticmethod
    def get(request):
        dialogues = Dialogue.objects.filter(Q(creator=request.user) | Q(invited=request.user))
        dialogue_serializer = DialogueSerializers(dialogues, many=True).data

        tracking_user(request)

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

        tracking_user(request)

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

        dialogues = Dialogue.objects.filter(id=dialogue_id)
        dialogue_serializer = DialogueSerializers(dialogues, many=True).data

        creator = dialogue_serializer[0]["creator"]["username"]
        invited = dialogue_serializer[0]["invited"]["username"]

        if str(request.user) == creator:
            invited_user = invited
        else:
            invited_user = creator

        dialogues = Dialogue.objects.filter(Q(creator=request.user) & Q(id=dialogue_id) | Q(invited=request.user) & Q(id=dialogue_id))

        tracking_user(request)

        user = User.objects.filter(username=invited_user)

        date = TrackingUser.objects.filter(user=user[0])[0].date
        difference = datetime.now(timezone.utc) - date
        support = timedelta(seconds=10)
        if difference < support:
            is_online = {"is_online": difference < support, "date": ""}
        elif str(date)[:10] == str(datetime.now(timezone.utc))[:10]:
            is_online = {"is_online": difference < support, "date": f"Сегодня {str(date + timedelta(hours=3))[11:16]}"}
        elif str(date + timedelta(days=1))[:10] == str(datetime.now(timezone.utc))[:10]:
            is_online = {"is_online": difference < support, "date": f"Вчера {str(date + timedelta(hours=3))[11:16]}"}
        elif str(date)[:4] == str(datetime.now(timezone.utc))[:4]:
            month = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']

            time = str(date + timedelta(hours=3))[5:16]
            time_fix = f"{time[3:5]} {month[int(time[:2]) - 1]} {time[6:]}"

            is_online = {"is_online": difference < support, "date": time_fix}
        else:
            is_online = {"is_online": difference < support, "date": str(date + timedelta(hours=3))[:16]}

        if chat_dialogue:
            if str(request.user) != chat_dialogue_serializer[-1]["user"]["username"] and bool(chat_dialogue[len(chat_dialogue) - 1].is_read) is False:
                for i in range(len(chat_dialogue)):
                    if bool(chat_dialogue[i].is_read) is False:
                        chat_dialogue[i].is_read = True
                        chat_dialogue[i].save()

        if dialogues:
            if chat_dialogue:
                if str(request.user) != chat_dialogue_serializer[-1]["user"]["username"] and bool(dialogues[0].is_read) is False:
                    dialogues[0].is_read = True
                    dialogues[0].save()

            for index_odict in range(len(chat_dialogue_serializer)):
                chat_dialogue_serializer[index_odict]["user"] = chat_dialogue_serializer[index_odict]["user"]["username"]

            return Response({"online": is_online, "data": chat_dialogue_serializer})
        return Response({"data": "Вы не состоите в диалоге."}, status=400)

    @staticmethod
    def post(request):
        chat = ChatPostSerializers(data=request.data)
        dialogue_id = request.data.get("dialogue")

        tracking_user(request)

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

        tracking_user(request)

        search = User.objects.filter(username__icontains=request.GET.get("user")).exclude(username=request.user)
        search_serializers = UserNameSerializers(search, many=True).data

        if search:
            scrolling_options = []
            five_options = []
            for odict in search_serializers:
                five_options += [odict]
                if len(five_options) == 5:
                    scrolling_options += [five_options]
                    five_options = []
            if five_options:
                scrolling_options += [five_options]

            return Response({"quantity": len(scrolling_options), "data": scrolling_options[scroll_number - 1]}, status=201)
        return Response({"quantity": 1, "data": [{"username": "Пользователь не найден."}]}, status=201)
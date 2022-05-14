from django.db import models

from django.contrib.auth.models import User

class Dialogue(models.Model):
    # Модель диалога
    creator = models.ForeignKey(User, verbose_name="Создатель", related_name="creator", on_delete=models.CASCADE)
    invited = models.ForeignKey(User, verbose_name="Участники", related_name="invited", on_delete=models.CASCADE, null=True)
    date = models.DateTimeField("Дата создания", auto_now_add=True)
    is_read = models.BooleanField("Прочитано", default=False)

    class Meta:
        verbose_name = "Диалог"
        verbose_name_plural = "Диалоги"


class ChatToDialogue(models.Model):
    # Модель чата, привязанная к диалогу
    dialogue = models.ForeignKey(Dialogue, verbose_name="Диалог", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    message = models.TextField("Сообщение", max_length=500)
    date = models.DateTimeField("Дата отправки", auto_now_add=True)
    is_read = models.BooleanField("Прочитано", default=False)

    class Meta:
        verbose_name = "Сообщение диалога"
        verbose_name_plural = "Сообщения диалогов"

class TrackingUser(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    date = models.DateTimeField("Дата отправки запроса", auto_now=True)

    class Meta:
        verbose_name = "Последняя активность"
        verbose_name_plural = "Последняя активность"

class Discussion(models.Model):
    # Модель беседы
    creator = models.ForeignKey(User, verbose_name="Создатель", related_name="user_creator", on_delete=models.CASCADE)
    invited = models.ManyToManyField(User, verbose_name="Участники", related_name="users_invited")
    date = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Беседа"
        verbose_name_plural = "Беседы"


class ChatToDiscussion(models.Model):
    # Модель чата, привязанная к беседе
    dialogue = models.ForeignKey(Discussion, verbose_name="Беседа", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    message = models.TextField("Сообщение", max_length=500)
    date = models.DateTimeField("Дата отправки", auto_now_add=True)

    class Meta:
        verbose_name = "Сообщение беседы"
        verbose_name_plural = "Сообщения бесед"
from django.contrib import admin
from .models import Dialogue, ChatToDialogue  # , Discussion, ChatToDiscussion


class DialogueAdmin(admin.ModelAdmin):
    list_display = ("id", "creator", "invited", "is_read", "date")


class ChatToDialogueAdmin(admin.ModelAdmin):
    list_display = ("id", "dialogue", "user", "message", "date")


class DiscussionAdmin(admin.ModelAdmin):
    list_display = ("id", "creator", "users_invited", "date")

    @staticmethod
    def users_invited(obj):
        return "\n".join([user.username for user in obj.invited.all()])


class ChatToDiscussionAdmin(admin.ModelAdmin):
    list_display = ("id", "dialogue", "user", "message", "date")


admin.site.register(Dialogue, DialogueAdmin)
admin.site.register(ChatToDialogue, ChatToDialogueAdmin)

# admin.site.register(Discussion, DiscussionAdmin)
# admin.site.register(ChatToDiscussion, ChatToDiscussionAdmin)

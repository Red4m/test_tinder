from django.contrib import admin

from message.models import Message


@admin.register(Message)
class MatchAdmin(admin.ModelAdmin):
    list_display = ("match_dialog_id", )

from django.contrib.auth.models import User
from django.db import models

from match.models import Match


class Message(models.Model):
    chat_messages_text = models.TextField()
    match_dialog_id = models.OneToOneField(
        Match,
        on_delete=models.CASCADE,
        related_name="match_dialog_id",
        null=True,
    )



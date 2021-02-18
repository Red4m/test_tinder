from django.contrib.auth.models import User
from django.db import models


class Match(models.Model):
    first_person_status = models.BooleanField(default=False)
    second_person_status = models.BooleanField(default=False)
    first_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="first_id",
        null=True,
        blank=True
    )
    second_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="second_id",
        null=True,
        blank=True
    )


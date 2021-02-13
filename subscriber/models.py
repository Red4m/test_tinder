from django.db import models


class Subscriber(models.Model):
    type_subscriber = models.CharField(max_length=80,
                                       verbose_name="type_subscriber",
                                       default="standart")
    swipes = models.IntegerField(verbose_name="swipes", default="20")
    radius = models.IntegerField(verbose_name="radius", default="10")

    def __str__(self):
        return self.type_subscriber

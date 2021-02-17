from django.db import models


class Subscriber(models.Model):
    SUBSCRIBE_CHOICES = (
        ('standart', 'standart'),
        ('vip', 'vip'),
        ('premium', 'premium')
    )
    a = 1000
    b = 1000
    NEW_CHOICES = {
        'standart':
            {
                'swipes': 20,
                'radius': 10
            },
        'vip':
            {
                'swipes': 100,
                'radius': 25
            },
        'premium':
            {
                'swipes': b,
                'radius': a
            }
    }
    type_subscriber = models.CharField(max_length=80,
                                       verbose_name="type_subscriber",
                                       choices=SUBSCRIBE_CHOICES,
                                       default="standart", null=True)
    swipes = models.IntegerField(null=True)
    radius = models.IntegerField(null=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.type_subscriber == 'standart' or self.type_subscriber == 'vip':
            self.swipes = self.NEW_CHOICES[self.type_subscriber]['swipes']
            print(self.swipes)
            self.radius = self.NEW_CHOICES[self.type_subscriber]['radius']
            print(self.radius)
        super().save(force_insert=force_insert, force_update=force_update, using=using,
             update_fields=update_fields)


    def __str__(self):
        return self.type_subscriber

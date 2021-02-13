from django.contrib import admin

# Register your models here.
from subscriber.models import Subscriber


@admin.register(Subscriber)
class MatchAdmin(admin.ModelAdmin):
    list_display = ("type_subscriber",)

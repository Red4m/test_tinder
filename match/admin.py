from django.contrib import admin

from match.models import Match


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ("status", )


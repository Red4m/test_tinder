

from django.contrib import admin
from django.contrib.auth.models import User

from profile.models import Profile, Image


# class ImageAdmin(admin.TabularInline):
#     model = Image
#
#
# class ProfileAdmin(admin.ModelAdmin):
#     inlines = [
#         ImageAdmin,
#     ]
#
#     class Meta:
#         model = User
#
#
# admin.site.register(User, ProfileAdmin)
#
# admin.site.register(Image)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("description", )


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("image_file", "obj", )
    list_editable = ('obj',)


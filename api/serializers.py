from rest_framework import serializers
from django.urls import reverse
from django.contrib.auth.models import User

from profile.models import Profile, Image


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ['obj', 'image_file', ]


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['description', ]


class UserSerializer(serializers.ModelSerializer):
    # images = serializers.SerializerMethodField()
    # images = ImageSerializer()
    link = serializers.SerializerMethodField()
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'link', 'profile',
                  ]

    # def get_image(self, obj):
    #     images = Image.objects.all().filter(obj=obj)
    #     s = ImageSerializer(images, many=True, context=self.context)
    #     return s.data
    #
    # def get_articles(self, obj):
    #     articles = Article.objects.all().filter(author=obj)
    #     s = ArticleSerializer(articles, many=True, context=self.context)
    #     return s.data

    def get_link(self, obj):
        uri = reverse('users-detail', kwargs={'username': obj.username})
        return self.context['request'].build_absolute_uri(uri)

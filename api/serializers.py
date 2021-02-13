from rest_framework import serializers
from django.urls import reverse
from django.contrib.auth.models import User

from match.models import Match
from message.models import Message
from profile.models import Profile, Image
from subscriber.models import Subscriber


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = [
            'id',
            'match_dialog_id',
            'message_user_id',
            'message_to_user_id',
            'chat_messages_text'
                  ]


class MatchSerializer(serializers.ModelSerializer):
    message = serializers.SerializerMethodField()
    link = serializers.SerializerMethodField()

    class Meta:
        model = Match
        fields = ['id', 'status', 'first_id', 'second_id', 'message', 'link']

    def get_link(self, obj):
        uri = reverse('match-detail', kwargs={'username': obj.first_id})
        return self.context['request'].build_absolute_uri(uri)

    def update(self, instance, validated_data):
        request = self.context.get('request')
        user = request.user
        if user.is_authenticated and instance.first_id == user.id:
            return super(MatchSerializer, self).update(instance,
                                                         validated_data)
        raise Exception('No credentials')

    def get_message(self, obj):
        message = Message.objects.all().filter(match_dialog_id=obj.id)
        s = MessageSerializer(message, many=True, context=self.context)
        return s.data


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ['image_file', 'obj']


class SubscriberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscriber
        fields = ['type_subscriber', 'swipes', 'radius']


class ProfileSerializer(serializers.ModelSerializer):
    subscriber = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['id', 'description', 'subscriber']

    def get_subscriber(self, obj):
        subscriber = Subscriber.objects.all().filter(type_subscriber=obj.type_of_subscriber)
        s = SubscriberSerializer(subscriber, many=True, context=self.context)
        return s.data


class UserSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    # images = ImageSerializer()
    match = serializers.SerializerMethodField()
    # message = serializers.SerializerMethodField()
    link = serializers.SerializerMethodField()
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'link', 'profile', 'images', 'match',
                  ]

    def get_images(self, obj):
        images = Image.objects.all().filter(obj=obj)
        s = ImageSerializer(images, many=True, context=self.context)
        return s.data

    def get_match(self, obj):
        match = Match.objects.all().filter(first_id=obj)
        s = MatchSerializer(match, many=True, context=self.context)
        return s.data

    # def get_message(self, obj):
    #     message = Message.objects.all().filter(obj=obj)
    #     s = ImageSerializer(message, many=True, context=self.context)
    #     return s.data
    #
    # def get_articles(self, obj):
    #     articles = Article.objects.all().filter(author=obj)
    #     s = ArticleSerializer(articles, many=True, context=self.context)
    #     return s.data

    def get_link(self, obj):
        uri = reverse('users-detail', kwargs={'username': obj.username})
        return self.context['request'].build_absolute_uri(uri)

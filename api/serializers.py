from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.urls import reverse
from django.contrib.auth.models import User

from match.models import Match
from message.models import Message
from profile.models import Profile, Image
from subscriber.models import Subscriber


class MessageSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = [
            'id',
            'match_dialog_id',
            'chat_messages_text',
            'link'
                  ]

    def save(self, **kwargs):
        print(self.data)

    def update(self, instance, validated_data):
        request = self.context.get('request')
        user = request.user
        if user.is_authenticated:
            return super(MessageSerializer, self).update(instance,
                                                         validated_data)
        raise Exception('No credentials')

    def get_link(self, obj):
        uri = reverse('message-detail', kwargs={'pk': obj.pk})
        return self.context['request'].build_absolute_uri(uri)


class MatchSerializer(serializers.ModelSerializer):
    message = serializers.SerializerMethodField()
    link = serializers.SerializerMethodField()

    class Meta:
        model = Match
        fields = ['id',
                  'first_person_status',
                  'second_person_status',
                  'first_id', 'second_id',
                  'message',
                  'link'
                  ]

    def get_link(self, obj):
        uri = reverse('match-detail', kwargs={'pk': obj.id})
        return self.context['request'].build_absolute_uri(uri)

    def update(self, instance, validated_data):
        request = self.context.get('request')
        print(request)
        user = request.user
        print(user)
        if user.is_authenticated:
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
    profile_link = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['id', 'description', 'subscriber', 'latitude', 'longitude', 'profile_link']

    def update(self, instance, validated_data):
        request = self.context.get('request')
        user = request.user
        if user.is_authenticated:
            return super(ProfileSerializer, self).update(instance,
                                                         validated_data)
        raise Exception('No credentials')

    def get_profile_link(self, obj):
        uri = reverse('profile-detail', kwargs={'pk': obj.pk})
        return self.context['request'].build_absolute_uri(uri)

    def get_subscriber(self, obj):
        subscriber = Subscriber.objects.all().filter(type_subscriber=obj.type_of_subscriber)
        s = SubscriberSerializer(subscriber, many=True, context=self.context)
        return s.data


class UserSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    match = serializers.SerializerMethodField()
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

    def update(self, instance, validated_data):
        request = self.context.get('request')
        user = request.user
        if user.is_authenticated:
            return super(UserSerializer, self).update(instance, validated_data)
        raise Exception('No credentials')

    def get_link(self, obj):
        uri = reverse('users-detail', kwargs={'username': obj.username})
        return self.context['request'].build_absolute_uri(uri)


class RegistrySerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'username', 'email', 'password', 'password2',
        ]

    def create(self, validated_data):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password == password2:
            user = User.objects.create_user(
                username=validated_data['username'],
                email=validated_data['email'],
            )
            user.set_password(password)
            user.save()
            return user
        else:
            raise serializers.ValidationError(
                {"password": "Password are not the same"}
            )

from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from api.permissions import IsUserOrReadOnly
from api.serializers import UserSerializer, MessageSerializer, MatchSerializer, \
    RegistrySerializer, ProfileSerializer
from match.models import Match
from message.models import Message
from profile.models import Profile


class UserViewSet(ModelViewSet):
    permission_classes = (IsAdminUser, IsUserOrReadOnly, )
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "username"
    # pagination_class = LimitOffsetPagination


class MatchViewSet(ModelViewSet):
    # permission_classes = (IsAuthorOrReadOnly )
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    lookup_field = "pk"
    # pagination_class = CustomPageNumberPagination
    # filter_backends = (SearchFilter, )
    # search_fields = ('status', 'id')


class RegistryView(CreateAPIView):
    serializer_class = RegistrySerializer


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    lookup_field = "pk"


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = "pk"

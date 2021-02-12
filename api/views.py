from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from api.permissions import IsUserOrReadOnly
from api.serializers import UserSerializer, MessageSerializer, MatchSerializer
from match.models import Match
from message.models import Message


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
    lookup_field = "match"
    # pagination_class = CustomPageNumberPagination
    # filter_backends = (SearchFilter, )
    # search_fields = ('status', 'id')

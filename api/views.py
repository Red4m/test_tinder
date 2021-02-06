from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from api.permissions import IsUserOrReadOnly
from api.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    permission_classes = (IsAdminUser, IsUserOrReadOnly, )
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "username"
    # pagination_class = LimitOffsetPagination

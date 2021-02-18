from rest_framework.routers import DefaultRouter
from django.urls import path, include

from api import views

router = DefaultRouter()
router.register('users', views.UserViewSet, basename="users")
router.register('match', views.MatchViewSet, basename="match")
router.register('message', views.MessageViewSet, basename="message")
router.register('profile', views.ProfileViewSet, basename="profile")
urlpatterns = [
    path('', include(router.urls)),
    path('sign-up', views.RegistryView.as_view())
    ]

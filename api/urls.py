from rest_framework.routers import DefaultRouter
from django.urls import path, include

from api import views

router = DefaultRouter()
# router.register('articles', views.ArticleViewSet, basename="articles")
router.register('users', views.UserViewSet, basename="users")

urlpatterns = [
    path('', include(router.urls)),
    ]
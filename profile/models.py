from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)

from subscriber.models import Subscriber


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    description = models.TextField(verbose_name="description")
    type_of_subscriber = models.ForeignKey(
        Subscriber,
        on_delete=models.CASCADE,
        related_name="type_of_subscriber",
        null=True,
        blank=True
    )
    ip_address = models.GenericIPAddressField(null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)

    def __str__(self):
        return self.user.username


class Image(models.Model):
    image_file = models.ImageField(upload_to="images/", null=True, blank=True)
    obj = models.ForeignKey(User, on_delete=models.CASCADE)


# class UserManager(BaseUserManager):
#
#     # def _create_user(self, email, password, **extra_fields):
#     #     if not email:
#     #         raise ValueError('The given email must be set')
#     #         try:
#     #             with transaction.atomic():
#     #                 user = self.model(email=email, **extra_fields)
#     #                 user.set_password(password)
#     #                 user.save(using=self._db)
#     #                 return user
#     #         except:
#     #             raise
#
#     def create_user(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, **extra_fields)
#
#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self._create_user(email, password=password, **extra_fields)
#
#
# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(max_length=40, unique=True)
#     first_name = models.CharField(max_length=30, blank=True)
#     last_name = models.CharField(max_length=30, blank=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(default=timezone.now)
#
#     objects = UserManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name']
#
#     def save(self, *args, **kwargs):
#         super(User, self).save(*args, **kwargs)
#         return self






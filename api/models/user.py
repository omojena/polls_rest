from django.contrib.auth.base_user import AbstractBaseUser

from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

from api.models.user_manager import UserManager


class User(AbstractBaseUser):
    class UserType(models.IntegerChoices):
        USER = 1
        ADMIN = 2
        SUPER_ADMIN = 3

    userType = models.IntegerField(choices=UserType.choices, default=UserType.USER)
    username = models.CharField(max_length=255, unique=True, db_index=True)
    full_name = models.CharField(max_length=255, blank=True)
    avatar = models.TextField(blank=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'

    objects = UserManager()

    def __str__(self):
        return self.username

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

from django.contrib.auth.base_user import AbstractBaseUser

from django.db import models


class User(AbstractBaseUser):
    class UserType(models.IntegerChoices):
        USER = 1
        ADMIN = 2
        SUPER_ADMIN = 3

    userType = models.IntegerField(choices=UserType.choices, default=UserType.USER)
    username = models.CharField(max_length=255, unique=True, db_index=True)
    full_name = models.CharField(max_length=255, blank=True)
    avatar = models.TextField()
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

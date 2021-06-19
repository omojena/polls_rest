from django.db import models
from django.contrib.postgres.fields import HStoreField

from api.models.user import User


class Polls(models.Model):
    title = models.CharField(max_length=255)
    options = HStoreField()
    total_votes = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_votes = models.ManyToManyField(User, blank=True, related_name='User_Votes')

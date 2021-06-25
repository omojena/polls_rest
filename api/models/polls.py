from api.models.options_poll import OptionsPoll

try:
    from django.db.models import JSONField

except:
    from django.contrib.postgres.fields import JSONField, ArrayField
from django.db import models


class Polls(models.Model):
    title = models.CharField(max_length=255)
    total_votes = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_votes = models.ManyToManyField('User', blank=True, related_name='User_Votes')

    @property
    def options(self):
        return OptionsPoll.objects.filter(fk_poll=self.id)

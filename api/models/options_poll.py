from django.db import models


class OptionsPoll(models.Model):
    title = models.CharField(max_length=255)
    percentage = models.FloatField(default=0.0)
    total_votes = models.PositiveIntegerField(default=0)
    fk_poll = models.ForeignKey('Polls', models.DO_NOTHING)

from rest_framework import serializers

from api.models.options_poll import OptionsPoll
from api.serializers.poll_serializer import PollSerializer


class OptionPollSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionsPoll
        fields = ['id', 'title', 'percentage', 'total_votes', 'fk_poll']


class OptionPollSerializerList(serializers.ModelSerializer):
    fk_poll = PollSerializer()

    class Meta:
        model = OptionsPoll
        fields = ['id', 'title', 'percentage', 'total_votes', 'fk_poll']

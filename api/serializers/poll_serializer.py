from api.models.options_poll import OptionsPoll
from rest_framework import serializers

from api.models.polls import Polls
from api.serializers.user_serializer import UserSerializer


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionsPoll
        fields = ['id', 'title', 'percentage', 'total_votes', 'fk_poll']


class PollSerializerList(serializers.ModelSerializer):
    user_votes = UserSerializer(read_only=True, many=True)
    options = OptionSerializer(many=True, allow_null=True)

    class Meta:
        model = Polls
        fields = ['id', 'title', 'total_votes', 'is_active', 'created_at', 'updated_at', 'user_votes', 'options']


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polls
        fields = ['id', 'title', 'total_votes', 'is_active', 'created_at', 'updated_at', 'user_votes']

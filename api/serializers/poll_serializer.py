from rest_framework import serializers

from api.models.polls import Polls
from api.serializers.user_serializer import UserSerializer


class PollSerializer(serializers.ModelSerializer):
    user_votes = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Polls
        fields = ['id', 'title', 'options', 'total_votes', 'is_active', 'created_at', 'updated_at', 'user_votes']

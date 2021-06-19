from rest_framework import serializers

from api.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'userType', 'username', 'full_name', 'avatar', 'is_staff', 'created_at', 'updated_at']
        read_only_fields = ['id']

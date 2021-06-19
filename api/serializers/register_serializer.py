from rest_framework import serializers

from api.models.user import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ["username", "password", "full_name", "avatar"]

    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        avatar = validated_data["avatar"]
        full_name = validated_data["full_name"]

        user = User.objects.create_user(password=password, username=username, avatar=avatar, full_name=full_name)
        return user

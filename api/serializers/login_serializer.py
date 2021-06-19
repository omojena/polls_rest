from rest_framework import serializers
from django.contrib import auth
from api.models.user import User
from rest_framework.exceptions import AuthenticationFailed


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    username = serializers.CharField(
        max_length=255, min_length=3, write_only=True)

    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = User.objects.get(username=obj['username'])

        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    class Meta:
        model = User
        fields = ['id', 'password', 'full_name', 'userType', 'avatar', 'username', 'tokens']

    def validate(self, attrs):
        username = attrs.get('username', '')
        password = attrs.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')

        return {
            'id': user.id,
            'full_name': user.full_name,
            'username': user.username,
            'avatar': user.avatar,
            'tokens': user.tokens,
            'is_active': user.is_active,
            'userType': user.userType
        }

        return super().validate(attrs)

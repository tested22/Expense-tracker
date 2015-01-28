from django.contrib.auth import get_user_model
try:
    from django.utils.http import urlsafe_base64_decode as uid_decoder
except:
    from django.utils.http import base36_to_int as uid_decoder
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class LoginSerializer(AuthTokenSerializer):
    def validate(self, attrs):
        attrs = super(LoginSerializer, self).validate(attrs)
        return attrs


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key',)


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name')
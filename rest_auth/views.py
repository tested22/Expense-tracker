from django.contrib.auth import login, logout
from django.conf import settings

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.generics import RetrieveUpdateAPIView

from .app_settings import (TokenSerializer,
    LoginSerializer, UserDetailsSerializer)

class Login(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    token_model = Token
    response_serializer = TokenSerializer

    def login(self):
        self.user = self.serializer.validated_data['user']
        self.token, created = self.token_model.objects.get_or_create(
            user=self.user)
        if getattr(settings, 'REST_SESSION_LOGIN', True):
            login(self.request, self.user)


    def get_response(self):
        return Response(self.response_serializer(self.token).data,
            status=status.HTTP_200_OK)

    def get_error_response(self):
        return Response(self.serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=self.request.DATA)
        if not self.serializer.is_valid():
            return self.get_error_response()
        self.login()
        return self.get_response()


class Logout(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            request.user.auth_token.delete()
        except:
            pass

        logout(request)

        return Response({"success": "Successfully logged out."},
                        status=status.HTTP_200_OK)


class UserDetails(RetrieveUpdateAPIView):
    serializer_class = UserDetailsSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


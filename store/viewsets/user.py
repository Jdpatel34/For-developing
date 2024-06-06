
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.generics import *
from store.models import LoginUser
from store.serializers.user import LoginUserSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginUserViewSet(viewsets.ModelViewSet, CreateAPIView):
    queryset = LoginUser.objects.all()
    serializer_class = LoginUserSerializer

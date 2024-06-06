from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import serializers
from rest_framework.response import Response
from store.models import LoginUser
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.status import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginUser
        fields = '__all__'
    
    def create(self, validated_data):
        email_id = validated_data['email']
        mobile_no = validated_data['mobile_no']
        username = validated_data['username']
        obj = LoginUser.objects.all().filter(username__exact=username, mobile_no__exact=mobile_no, email__exact=email_id)
        if obj:
            raise serializers.ValidationError('This User details are already exists!!', code=HTTP_404_NOT_FOUND)
        return super().create(validated_data)

class ProtectedView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "This is a protected view."})


from django.shortcuts import render
from rest_framework.views import APIView
from users.api.serializers import RegistrationSerializer,LoginSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class UserRegistrationView(APIView):
    def post(self,request):
        serializer=RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors)
    
class LogoutView(APIView):
    def post(self,request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=200)
        except Exception as e:
            return Response(status=400)
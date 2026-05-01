from django.shortcuts import render
from rest_framework.views import APIView
from users.api.serializers import RegistrationSerializer,LoginSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class UserRegistrationView(APIView):
    def post(self,request):
        print("register")
        serializer=RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            if User.objects.get(username=serializer.validated_data["username"]):
                return Response({"error" : "User already exists"})
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors)

class UserLoginView(APIView):
    def post(self,request):
        print("LOGIN")
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user=User.objects.get(username=request.data["username"])
            except:
                return Response({"error":"invalid details"})
            if user.check_password(request.data["password"]): 
                token=RefreshToken.for_user(user)
                data={
                    "refresh":str(token),
                    "access":str(token.access_token)
                }
                return Response(data)
            return Response({"error":"invalid password"})
        return Response(serializer.errors)                
    
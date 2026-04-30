from django.shortcuts import render
from rest_framework.views import APIView
from users.api.serializers import RegistrationSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
# Create your views here.

class UserRegistrationView(APIView):
    def post(self,request):
        serializer=RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.validated_data["password"]!=serializer.validated_data["password2"]:
                return Response({"error":"passwords do not match"})
            elif User.objects.filter(username=serializer.validated_data["username"]).exists():
                return Response({"error" : "User already exists"})
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors)
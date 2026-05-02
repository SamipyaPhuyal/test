from django.shortcuts import render
from rest_framework.views import generics
from .api.serializers import StudentSerializer
from .models import Student
from rest_framework.response import Response
# Create your views here.
class StudentListView(generics.ListCreateAPIView):
    def get_queryset(self):
        return Student.objects.all()
    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=200)
        return Response(serializer.errors)
    
from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ViewSet,ModelViewSet
from .api.serializers import StudentSerializer
from .models import Student
from rest_framework.response import Response
# Create your views here.
class StudentListView(generics.ListCreateAPIView):
    serializer_class=StudentSerializer
    def get_queryset(self):
        return Student.objects.all()
    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success":"status=200"})
        return Response(serializer.errors)
    
class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=StudentSerializer
    def get_queryset(self):
        return Student.objects.all()
    
class StudentSet(ModelViewSet):
    serializer_class=StudentSerializer
    queryset=Student.objects.all()
    
class GenericView(generics.ListCreateAPIView):
   queryset=Student.objects.all()
   serializer_class=StudentSerializer
   
    
    
    
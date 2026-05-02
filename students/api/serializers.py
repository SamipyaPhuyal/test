from rest_framework.serializers import serializers
from students.views import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.views import Response


class RegistrationSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    password2=serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields=["password","password2","id","username"]
        extra_kwargs = {
            'id': {'read_only': True}
        }

    def create(self,validated_data):
        user=User.objects.create_user(
        username=validated_data["username"],
        password=validated_data["password"]        
        )
        return user
class LoginSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields=["username","password"]
        
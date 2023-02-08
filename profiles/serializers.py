from rest_framework import serializers
from django.contrib.auth.models import User

from profiles.models import Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username'] 


class ProfileReadSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['user', 'bio', 'image', 'created_at'] 

class ProfileWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'bio', 'image', 'created_at'] 


from rest_framework import serializers
from django.contrib.auth.models import User

from profiles.models import Profile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = '__all__'


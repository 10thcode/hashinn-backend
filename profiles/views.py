from rest_framework import viewsets
from django.contrib.auth.models import User

from profiles.models import Profile
from profiles.serializers import ProfileReadSerializer, ProfileWriteSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Profile.objects.filter(id=self.request.user.id)

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ProfileReadSerializer
        else:
            return ProfileWriteSerializer


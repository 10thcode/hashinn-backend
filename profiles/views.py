from rest_framework import viewsets

from profiles.models import Profile
from profiles.serializers import ProfileReadSerializer, ProfileWriteSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ProfileReadSerializer
        else:
            return ProfileWriteSerializer


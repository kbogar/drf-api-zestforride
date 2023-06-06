from django.http import Http404
from rest_framework import status
from rest_framework import generics
from zestforride_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django-signals.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.ListAPIView):
    """
    Retrieve or update a profile if you are the owner.
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()

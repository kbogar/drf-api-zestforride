from rest_framework import generics, permissions, filters
from zestforride_api.permissions import IsOwnerOrReadOnly
from .models import Event
from .serializers import EventSerializer
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend


class EventList(generics.ListCreateAPIView):
    """
    List events or create an event if logged in
    The perform_create method associates the event with the logged in user.
    """
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Event.objects.annotate(
        interested_count=Count('interested', distinct=True),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    search_fields = [
        'owner__username',
        'name',
        'event_details',
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'interested__owner__profile',
        'owner__profile',
    ]
    ordering_fields = [
        'interested_count',
        'interested__created_at',
        'date',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve an event and edit or delete it if you own it.
    """
    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Event.objects.annotate(
        interested_count=Count('interested', distinct=True),
    ).order_by('-created_at')

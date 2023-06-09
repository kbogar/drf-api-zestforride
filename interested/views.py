from rest_framework import generics, permissions
from zestforride_api.permissions import IsOwnerOrReadOnly
from .models import Interested
from .serializers import InterestedSerializer


class InterestedList(generics.ListCreateAPIView):
    """
    List Interested events or add interested
    if logged in
    """
    serializer_class = InterestedSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Interested.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class InterestedDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve interested event, or update or delete it
    by id if you are owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = InterestedSerializer
    queryset = Interested.objects.all()

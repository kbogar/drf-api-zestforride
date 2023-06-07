from rest_framework import generics, permissions
from .models import Contact
from .serializers import ContactSerializer


class ContactList(generics.ListCreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Contact.objects.all()

from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone


class Event(models.Model):
    """
    Event model, related to User.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50)
    event_details = models.TextField(blank=True)
    date = models.DateField(default=date.today)
    time = models.TimeField(default=timezone.now)
    image = models.ImageField(
        upload_to='images/', default='../default_upload_ba7oxe', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.name}'

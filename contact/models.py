from django.db import models


class Contact(models.Model):
    """
    Contact model
    """
    name = models.CharField(max_length=40)
    email = models.EmailField()
    subject = models.CharField(max_length=40)
    message = models.TextField(max_length=400, blank=True)

    def __str__(self):
        return str(self.name)

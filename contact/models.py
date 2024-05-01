# contact/models.py
from django.db import models
from django.utils import timezone


class Contact(models.Model):
    name = models.CharField(max_length=50)  # is this validation rule reasonable?
    email = models.EmailField(max_length=50)  # is this validation rule reasonable?
    # make subject options for a quick message
    # this feature was requested by many visitors
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField(max_length=2000)
    date_submitted = models.DateTimeField(default=timezone.now)

from django.db import models
from django.contrib.auth.models import User


class Traveler(models.Model):
    """Database model for a traveler"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=250)
    profile_image_url = models.CharField(max_length=100)
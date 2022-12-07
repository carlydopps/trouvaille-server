from django.db import models

class Destination(models.Model):
    """Database model for a destination"""
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
from django.db import models

class Duration(models.Model):
    """Database model for a duration"""
    extent = models.CharField(max_length=55)
from django.db import models

class Season(models.Model):
    """Database model for a season"""
    name = models.CharField(max_length=55)
from django.db import models

class ExperienceType(models.Model):
    """Database model for an experience type"""
    name = models.CharField(max_length=55)
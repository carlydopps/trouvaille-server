from django.db import models

class Style(models.Model):
    """Database model for a style"""
    name = models.CharField(max_length=55)
from django.db import models

class TripExperience(models.Model):
    """Database model for relationship between trips and experiences"""
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    experience = models.ForeignKey('Experience', on_delete=models.CASCADE)
    note = models.CharField(max_length=150)
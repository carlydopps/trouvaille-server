from django.db import models

class TripExperience(models.Model):
    """Database model for relationship between trips and experiences"""
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE, related_name="trip_trip_experiences")
    experience = models.ForeignKey('Experience', on_delete=models.CASCADE, related_name="experience_trip_experiences")
    note = models.CharField(max_length=150, default="")
from django.db import models

class TripDestination(models.Model):
    """Database model for relationship between trips and destinations"""
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    destination = models.ForeignKey('Destination', on_delete=models.CASCADE)
from django.db import models

class FavoriteTrip(models.Model):
    """Database model for a favorite trip"""
    trip = models.ForeignKey("Trip", on_delete=models.CASCADE, related_name='trip_favorited')
    traveler = models.ForeignKey("Traveler", on_delete=models.CASCADE, related_name='favorite_trips')
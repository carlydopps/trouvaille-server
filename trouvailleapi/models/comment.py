from django.db import models

class Comment(models.Model):
    """Database model for a comment on a trip"""
    trip = models.ForeignKey("Trip", on_delete=models.CASCADE, related_name='trip_comments')
    traveler = models.ForeignKey("Traveler", on_delete=models.CASCADE, related_name='traveler_comments')
    message = models.CharField(max_length = 150)
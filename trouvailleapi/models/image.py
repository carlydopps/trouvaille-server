from django.db import models

class Image(models.Model):
    """Database model for an image"""
    trip = models.ForeignKey("Trip", on_delete=models.CASCADE, related_name='trip_images')
    img_url = models.CharField(max_length=100)
    order = models.IntegerField(default=0)
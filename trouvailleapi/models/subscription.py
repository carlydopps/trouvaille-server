from django.db import models

class Subscription(models.Model):
    """Database model for a subscription"""
    follower = models.ForeignKey("Traveler", on_delete=models.CASCADE, related_name='follower_subscriptions')
    traveler = models.ForeignKey("Traveler", on_delete=models.CASCADE, related_name='traveler_subscriptions')
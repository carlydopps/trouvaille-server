from django.db import models
from trouvailleapi.models import Experience

class Trip(models.Model):
    """Database model for a trip"""
    title = models.CharField(max_length=50)
    summary = models.CharField(max_length=250)
    traveler = models.ForeignKey("Traveler", on_delete=models.CASCADE, related_name='traveled_trips')
    cover_img = models.CharField(max_length=100, default="")
    style = models.ForeignKey("Style", on_delete=models.CASCADE, related_name='styled_trips')
    season = models.ForeignKey("Season", on_delete=models.CASCADE, related_name='season_trips')
    duration = models.ForeignKey("Duration", on_delete=models.CASCADE, related_name='duration_trips')
    is_draft = models.BooleanField(default=True)
    is_upcoming = models.BooleanField(default=False)
    is_private = models.BooleanField(default=False)
    modified_date = models.DateTimeField()
    experiences = models.ManyToManyField('Experience', through='TripExperience', related_name='experience_trips')
    destinations = models.ManyToManyField('Destination', through='TripDestination', related_name='destination_trips') 

    @property
    def my_trip(self):
        return self.__my_trip

    @my_trip.setter
    def my_trip(self, value):
        self.__my_trip = value

    @property
    def favorite(self):
        return self.__favorite

    @favorite.setter
    def favorite(self, value):
        self.__favorite = value
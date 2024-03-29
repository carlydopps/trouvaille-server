from django.db import models
from django.contrib.auth.models import User


class Traveler(models.Model):
    """Database model for a traveler"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=250)
    profile_img = models.CharField(max_length=500)
    cover_img = models.CharField(max_length=500, default="")

    @property
    def first_name(self):
        return f'{self.user.first_name}'

    @property
    def last_name(self):
        return f'{self.user.last_name}'

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @property
    def username(self):
        return f'{self.user.username}'

    @property
    def following(self):
        return self.__following

    @following.setter
    def following(self, value):
        self.__following = value

    @property
    def myself(self):
        return self.__myself

    @myself.setter
    def myself(self, value):
        self.__myself = value

    @property
    def follower_count(self):
        followers = self.traveler_subscriptions.all()
        total = len(followers)
        return total
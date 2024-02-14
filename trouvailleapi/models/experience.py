from django.db import models

class Experience(models.Model):
    """Database model for a experience"""
    title = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    website_url = models.CharField(max_length=250)
    experience_type = models.ForeignKey("ExperienceType", on_delete=models.CASCADE, related_name='experiences')
    image = models.CharField(max_length=500, default="")

    @property
    def favorite(self):
        return self.__favorite

    @favorite.setter
    def favorite(self, value):
        self.__favorite = value
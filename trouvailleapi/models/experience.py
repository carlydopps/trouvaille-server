from django.db import models

class Experience(models.Model):
    """Database model for a experience"""
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    website_url = models.CharField(max_length=100)
    experience_type = models.ForeignKey("ExperienceType", on_delete=models.CASCADE, related_name='experiences')
    image = models.CharField(max_length=100, default="")

    @property
    def favorite(self):
        return self.__favorite

    @favorite.setter
    def favorite(self, value):
        self.__favorite = value
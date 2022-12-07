from django.db import models

class Experience(models.Model):
    """Database model for a experience"""
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    website_url = models.CharField(max_length=50)
    experience_type = models.ForeignKey("ExperienceType", on_delete=models.CASCADE, related_name='experiences')
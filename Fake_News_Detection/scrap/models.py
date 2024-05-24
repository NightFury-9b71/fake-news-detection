from django.db import models

# Create your models here.

class news(models.Model):
    website = models.CharField(max_length=255)
    title = models.CharField(max_length=500)
    snippet = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return self.title


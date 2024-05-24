from django.db import models

# Create your models here.

class news(models.Model):
    site_name = models.CharField(max_length=255,null=True)
    title = models.CharField(max_length=500,null=True)
    snippet = models.TextField(null=True)
    link = models.URLField(null=True)
    search_timestamp = models.DateTimeField(auto_now_add=True)


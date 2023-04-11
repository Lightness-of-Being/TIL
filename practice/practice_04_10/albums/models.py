from django.db import models

# Create your models here.
class Album:
    content = models.CharField(max_length=20)
    image = models.ImageField(upload_to=None, blank=True)
from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=50)
    movie = models.CharField(max_length=50)
    content = models.TextField()
    
class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
from django.db import models

# Create your models here.
class Post(models.Model):
    user = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True)
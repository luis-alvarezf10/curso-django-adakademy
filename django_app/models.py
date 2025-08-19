from django.db import models

# Create your models here.

class Post(models.model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(blanck=True, null=True) 
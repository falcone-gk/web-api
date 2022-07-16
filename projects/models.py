from django.db import models

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=60)
    description = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    body = models.TextField()
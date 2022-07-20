from django.db import models

# Create your models here.

class Tag(models.Model):

    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Project(models.Model):

    title = models.CharField(max_length=60)
    description = models.TextField()
    created = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

class Post(models.Model):

    title = models.CharField(max_length=60)
    description = models.TextField()
    body = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
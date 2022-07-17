from django.db import models

# Create your models here.

class Project(models.Model):

    title = models.CharField(max_length=60)
    description = models.TextField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
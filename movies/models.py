from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    release_year = models.IntegerField()
    watched = models.BooleanField(default=False)

    def __str__(self):
        return self.title
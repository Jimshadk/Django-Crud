from django.db import models

class football(models.Model):
    club = models.CharField(max_length=200)
    manager = models.CharField(max_length=200)
    stadium = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    trophies = models.IntegerField()

    class Meta:
        db_table = "Football Clubs"

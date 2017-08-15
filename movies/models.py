from django.db import models


class Movies(models.Model):
    """A database to store information about movies."""
    id = models.AutoField(primary_key=True)
    year = models.IntegerField(blank=True, null=True)
    length = models.IntegerField(blank=True, null=True)
    title = models.TextField()
    subject = models.CharField(max_length=255, default='')
    actor = models.CharField(max_length=255, default='')
    actress = models.CharField(max_length=255, default='')
    director = models.CharField(max_length=255, default='')
    popularity = models.IntegerField(blank=True, null=True)
    awards = models.BooleanField()
    image = models.CharField(max_length=255, default='')

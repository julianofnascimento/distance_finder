from django.db import models

class DistanceSearch(models.Model):
    source_address = models.CharField(max_length=255)
    destination_address = models.CharField(max_length=255)
    distance_km = models.FloatField()
    search_date = models.DateTimeField(auto_now_add=True)

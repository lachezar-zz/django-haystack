from django.db import models

# Create your models here.

class SpatialTest(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    
"""
from django.contrib.gis.db import models
# Create your models here.

class SpatialTest(models.Model):
    name = models.CharField(max_length=100)
    point = models.PointField(srid=32140)
    objects = models.GeoManager()
"""
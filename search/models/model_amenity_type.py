from django.db import models

class AmenityType(models.Model):
    name = models.CharField(max_length = 20)
    
    class Meta:
        db_table = "amenity_types"
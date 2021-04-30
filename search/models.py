from django.db import models

class Amenity(models.Model):
    name         = models.CharField(max_length = 20)
    road_address = models.CharField(max_length = 20)
    legalcode    = models.CharField(max_length = 20)
    latitude     = models.DecimalField(max_digits = 15, decimal_places = 10) # 위도
    longitude    = models.DecimalField(max_digits = 15, decimal_places = 10) # 경도
    type         = models.ForeignKey("AmenityType", on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = "amenities"
        
class AmenityType(models.Model):
    name = models.CharField(max_length = 20)
    
    class Meta:
        db_table = "amenity_types"

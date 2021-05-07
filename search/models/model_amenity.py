from django.db import models

class Amenity(models.Model):
    name          = models.CharField(max_length = 20)
    regal_address = models.CharField(max_length = 500, null = True)
    road_address  = models.CharField(max_length = 500)
    latitude      = models.DecimalField(max_digits = 15, decimal_places = 10)
    longitude     = models.DecimalField(max_digits = 15, decimal_places = 10)
    amenity_type  = models.ForeignKey("AmenityType", on_delete = models.SET_NULL, null = True)
    dong          = models.ForeignKey("rooms.Dong",  on_delete = models.SET_NULL, null = True, related_name = "amenity")
    gu            = models.ForeignKey("rooms.Gu",    on_delete = models.SET_NULL, null = True, related_name = "amenity")
    
    class Meta:
        db_table = "amenities"
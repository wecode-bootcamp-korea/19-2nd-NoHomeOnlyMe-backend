from django.db import models

class Room(models.Model):
    name          = models.CharField(max_length=200)
    road_address  = models.CharField(max_length=500)
    regal_address = models.CharField(max_length=500, null = True)
    gu            = models.ForeignKey("Gu",   on_delete = models.SET_NULL, null = True)
    dong          = models.ForeignKey("Dong", on_delete = models.SET_NULL, null = True)
    apt_dong      = models.CharField(max_length=20, null=True)
    apt_ho        = models.CharField(max_length=20, null=True)
    room_type     = models.ForeignKey("RoomType",     on_delete=models.CASCADE, null = True)
    building_type = models.ForeignKey("BuildingType", on_delete=models.CASCADE, null = True)
    latitude      = models.DecimalField(max_digits=15, decimal_places=10)
    longitude     = models.DecimalField(max_digits=15, decimal_places=10)
    created_at    = models.DateTimeField(auto_now_add = True)
    updated_at    = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = "rooms"
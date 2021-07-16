from django.db import models

class Room(models.Model):
    apt_dong      = models.CharField(max_length=20, null=True)
    apt_ho        = models.CharField(max_length=20, null=True)
    name          = models.CharField(max_length=200)
    regal_address = models.CharField(max_length=500, null = True)
    road_address  = models.CharField(max_length=500)
    latitude      = models.DecimalField(max_digits=15, decimal_places=10)
    longitude     = models.DecimalField(max_digits=15, decimal_places=10)
    building_type = models.ForeignKey("BuildingType", on_delete=models.CASCADE, null = True, related_name = "rooms")
    dong          = models.ForeignKey("Dong", on_delete = models.SET_NULL, null = True, related_name = "rooms")
    gu            = models.ForeignKey("Gu", on_delete = models.SET_NULL, null = True, related_name = "rooms")
    room_type     = models.ForeignKey("RoomType", on_delete=models.CASCADE, null = True, related_name = "rooms")
    created_at    = models.DateTimeField(auto_now_add = True)
    updated_at    = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = "rooms"
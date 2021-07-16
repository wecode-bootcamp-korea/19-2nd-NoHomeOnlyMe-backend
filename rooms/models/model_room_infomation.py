from django.db import models

class RoomInformation(models.Model):
    exclusive_m2     = models.DecimalField(max_digits = 15, decimal_places = 5)
    supply_m2        = models.DecimalField(max_digits = 15, decimal_places = 5)
    heating_type     = models.ForeignKey("HeatingType",  on_delete = models.CASCADE)
    move_in_option   = models.ForeignKey("MoveInOption", on_delete = models.CASCADE)
    building_story   = models.IntegerField()
    exclusive_pyeong = models.IntegerField()
    floor            = models.IntegerField()
    supply_pyeong    = models.IntegerField()
    room             = models.OneToOneField("Room", on_delete = models.CASCADE, related_name = "room_info")
    
    class Meta:
        db_table = "room_informations"
from django.db import models

class RoomInformation(models.Model):
    supply_pyeong    = models.IntegerField()
    supply_m2        = models.DecimalField(max_digits=15, decimal_places=5)
    exclusive_pyeong = models.IntegerField()
    exclusive_m2     = models.DecimalField(max_digits=15, decimal_places=5)
    building_story   = models.IntegerField()
    floor            = models.IntegerField()
    heating_type     = models.CharField(max_length=50)
    move_in_date     = models.DateField(null=True)
    move_in_option   = models.ForeignKey("MoveInOption", on_delete=models.CASCADE)
    room             = models.ForeignKey("Room", on_delete=models.CASCADE, related_name = "room_info")
    
    class Meta:
        db_table = "room_informations"
        
class MoveInOption(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = "move_in_options"
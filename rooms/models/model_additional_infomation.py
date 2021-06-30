from django.db import models

class AdditionalInformation(models.Model):
    maintenance_cost         = models.DecimalField(max_digits = 18, decimal_places = 2, default = 0)
    parking_fee              = models.DecimalField(max_digits = 18, decimal_places = 2, default = 0)
    is_agreement             = models.BooleanField(default = False)
    room                     = models.ForeignKey("Room", on_delete = models.CASCADE)
    maintenance_cost_options = models.ManyToManyField("MaintenanceCostOption", through = "InclusionMaintenanceCost")
    additional_options       = models.ManyToManyField("AdditionalOption",      through = "CheckAdditionalOption")
    room_options             = models.ManyToManyField("RoomOption",            through = "AdditionalRoomOption")
    
    class Meta:
        db_table = "additional_informations"
        
class AdditionalOption(models.Model):
    name = models.CharField(max_length = 50)
    
    class Meta:
        db_table = "additional_options"

class MaintenanceCostOption(models.Model):
    name = models.CharField(max_length = 50)
    
    class Meta:
        db_table = "maintenance_cost_options"

class RoomOption(models.Model):
    name = models.CharField(max_length = 50)
    
    class Meta:
        db_table = "room_options"
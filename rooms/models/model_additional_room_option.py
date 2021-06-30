from django.db import models

class AdditionalRoomOption(models.Model):
    room_option            = models.ForeignKey("RoomOption", on_delete=models.CASCADE)
    additional_information = models.ForeignKey("AdditionalInformation", on_delete=models.CASCADE)
    
    class Meta:
        db_table = "additional_room_options"
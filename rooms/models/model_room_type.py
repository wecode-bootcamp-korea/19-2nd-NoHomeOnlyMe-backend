from django.db import models

class RoomType(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "room_types"
        

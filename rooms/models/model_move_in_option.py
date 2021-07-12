import datetime

from django.db import models

class MoveInOption(models.Model):
    name         = models.CharField(max_length=50)
    move_in_date = models.DateField(null = True)
    
    class Meta:
        db_table = "move_in_options"
        
    def __str__(self):
        return self.name
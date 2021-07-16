from django.db import models

class HeatingType(models.Model):
    name = models.CharField(max_length = 50)
    
    class Meta:
        db_table = "heating_types"
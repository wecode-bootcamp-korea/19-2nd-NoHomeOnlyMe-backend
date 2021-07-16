from django.db import models

class MaintenanceCostOption(models.Model):
    name = models.CharField(max_length = 50)
    
    class Meta:
        db_table = "maintenance_cost_options"
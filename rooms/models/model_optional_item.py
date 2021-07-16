from django.db import models

class OptionalItem(models.Model):
    name = models.CharField(max_length = 50)
    
    class Meta:
        db_table = "optional_items"
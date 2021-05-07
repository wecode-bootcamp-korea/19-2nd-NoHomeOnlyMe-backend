from django.db import models

class BuildingType(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "building_types"
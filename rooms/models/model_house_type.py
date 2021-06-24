from django.db import models

class HouseType(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "house_types"
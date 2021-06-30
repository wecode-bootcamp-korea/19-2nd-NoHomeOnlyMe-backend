from django.db import models

class SaleType(models.Model):
    name = models.CharField(max_length = 50)
    room = models.ManyToManyField("Room", through = "SaleInformation", related_name = "sale_types")
    
    class Meta:
        db_table = "sale_types"

class SaleInformation(models.Model):
    deposit     = models.DecimalField(max_digits = 18, decimal_places = 2)
    monthly_pay = models.DecimalField(max_digits = 18, decimal_places = 2, null = True)
    is_short    = models.BooleanField(default = False)
    sale_type   = models.ForeignKey("SaleType", on_delete = models.CASCADE)
    room        = models.ForeignKey("Room",     on_delete = models.CASCADE, related_name = "sale_info")

    class Meta:
        db_table = "sale_informations"
from decimal import Decimal

from django.db import models

class SaleType(models.Model):
    name = models.CharField(max_length = 100)
    
    class Meta:
        db_table = "sale_types"

class SaleInformation(models.Model):
    room        = models.ForeignKey("Room",     on_delete = models.CASCADE, related_name = "sale_info")
    sale_type   = models.ForeignKey("SaleType", on_delete = models.CASCADE)
    deposit     = models.DecimalField(max_digits = 18, decimal_places = 2)
    monthly_pay = models.DecimalField(max_digits = 18, decimal_places = 2, default = Decimal("000000.00"))
    is_short    = models.BooleanField(default = False)
    
    class Meta:
        db_table = "sale_informations"
from django.db import models

class AdditionalInformation(models.Model):
    STRUCTURE_CHOICES = (
        ("복층", "복층"),
        ("1.5룸/주방분리형", "1.5룸/주방분리형")
    )
    
    has_built_in            = models.BooleanField(default = False)
    has_elevator            = models.BooleanField(default = False)
    has_veranda             = models.BooleanField(default = False)
    is_able_deposit_loan    = models.BooleanField(default = False)
    is_able_park            = models.BooleanField(default = False)
    is_able_pet             = models.BooleanField(default = False)
    is_negotiable_mx_cost   = models.BooleanField(default = False)
    structure               = models.CharField(max_length = 10, choices = STRUCTURE_CHOICES, null = True)
    parking_fee             = models.DecimalField(max_digits = 18, decimal_places = 2, default = 0)
    maintenance_cost        = models.DecimalField(max_digits = 18, decimal_places = 2, default = 0)
    maintenance_cost_option = models.ManyToManyField("MaintenanceCostOption", through = "InclusionMaintenanceCost")
    optional_item           = models.ManyToManyField("OptionalItem",          through = "AdditionalInfoOptionalItem")
    room                    = models.OneToOneField("Room", on_delete = models.CASCADE, related_name = "additional_info")
    
    class Meta:
        db_table = "additional_informations"
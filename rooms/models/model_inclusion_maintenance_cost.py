from django.db    import models

class InclusionMaintenanceCost(models.Model):
    additional_information  = models.ForeignKey("AdditionalInformation", on_delete=models.CASCADE)
    maintenance_cost_option = models.ForeignKey("MaintenanceCostOption", on_delete=models.CASCADE)
    
    class Meta:
        db_table = "inclusion_maintenance_cost"
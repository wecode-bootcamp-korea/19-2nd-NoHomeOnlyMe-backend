from django.db import models

class AdditionalInfoOptionalItem(models.Model):
    additional_information = models.ForeignKey("AdditionalInformation", on_delete = models.CASCADE)
    optional_item          = models.ForeignKey("OptionalItem",          on_delete = models.CASCADE)
    
    class Meta:
        db_table = "additional_info_optional_items"
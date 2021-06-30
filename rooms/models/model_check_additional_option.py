from django.db import models

class CheckAdditionalOption(models.Model):
    is_able                = models.BooleanField(default=False) # 옵션 가능 여부
    additional_information = models.ForeignKey("AdditionalInformation", on_delete=models.CASCADE)
    additional_option      = models.ForeignKey("AdditionalOption", on_delete=models.CASCADE)

    class Meta:
        db_table = "check_additional_options"
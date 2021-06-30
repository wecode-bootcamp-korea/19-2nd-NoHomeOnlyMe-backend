from django.db import models

class DescriptionOption(models.Model):
    title       = models.CharField(max_length=300)
    description = models.TextField()
    secret_text = models.TextField()
    room        = models.ForeignKey("Room", on_delete=models.CASCADE)
    
    class Meta:
        db_table = "description_options"
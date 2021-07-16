from django.db import models

class Image(models.Model):
    image_url = models.CharField(max_length=2000)
    sequence  = models.IntegerField()
    room      = models.ForeignKey("Room", on_delete=models.CASCADE, related_name = "images")

    class Meta:
        db_table = "images"
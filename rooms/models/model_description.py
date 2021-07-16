from django.db import models

class Description(models.Model):
    title       = models.CharField(max_length=300)
    main_text   = models.TextField()
    secret_text = models.TextField(null = True)
    room        = models.OneToOneField("Room", on_delete=models.CASCADE)
    
    class Meta:
        db_table = "descriptions"
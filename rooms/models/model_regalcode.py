from django.db    import models

class Gu(models.Model):
    name      = models.CharField(max_length = 10)
    latitude  = models.DecimalField(max_digits = 15, decimal_places = 10)
    longitude = models.DecimalField(max_digits = 15, decimal_places = 10)
    
    class Meta:
        db_table = "gu"

# 주소지 동
class Dong(models.Model):
    name      = models.CharField(max_length = 10)
    latitude  = models.DecimalField(max_digits = 15, decimal_places = 10)
    longitude = models.DecimalField(max_digits = 15, decimal_places = 10)
    gu        = models.ForeignKey("Gu", null = True, on_delete = models.SET_NULL)
    
    class Meta:
        db_table = "dong"
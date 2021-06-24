from django.db    import models

class Gu(models.Model):
    name      = models.CharField(max_length=10)
    latitude  = models.DecimalField(max_digits=15, decimal_places=10) # 위도
    longitude = models.DecimalField(max_digits=15, decimal_places=10) # 경도
    
    class Meta:
        db_table = "gus"

# 주소지 동
class Dong(models.Model):
    name      = models.CharField(max_length=10)
    latitude  = models.DecimalField(max_digits=15, decimal_places=10) # 위도
    longitude = models.DecimalField(max_digits=15, decimal_places=10) # 경도
    gu        = models.ForeignKey("Gu", null=True, on_delete=models.SET_NULL)
    
    class Meta:
        db_table = "dongs"
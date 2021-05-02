from django.db import models

class User(models.Model):
    name         = models.CharField(max_length=50)
    email        = models.CharField(max_length=200)
    password     = models.CharField(max_length=1000)
    phone_number = models.CharField(max_length=20)
    homes        = models.ManyToManyField("homes.Home", through="Like", related_name="user_likes")
    user_code    = models.IntegerField(null = True)
    
    class Meta:
        db_table = "users"

class Like(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    home = models.ForeignKey("homes.Home", on_delete=models.CASCADE)

    class Meta:
        db_table = "likes"

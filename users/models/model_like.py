from django.db                  import models

class Like(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name = "like_user")
    home = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    class Meta:
        db_table = "likes"
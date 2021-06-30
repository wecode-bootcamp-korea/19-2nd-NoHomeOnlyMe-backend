from django.db                  import models
from django.utils.translation   import ugettext_lazy
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserManager(BaseUserManager):
    
    def create_user(self, **kwargs):
        
        if not kwargs['email']:
            raise ValueError(ugettext_lazy("Invalid ID"))
        
        user = self.model(
            email        = self.normalize_email(kwargs["email"]),
            name         = kwargs["name"],
            phone_number = kwargs["phone_number"],
        )
        user.set_password(kwargs["password"])
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, **kwargs):
        user = self.create_user(**kwargs)
        user.is_staff     = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
        
    class Meta:
        abstract = True
    
class User(AbstractBaseUser, PermissionsMixin):
    name         = models.CharField(max_length=50)
    email        = models.EmailField(max_length=200, unique = True)
    password     = models.CharField(max_length=1000, null = True)
    phone_number = models.IntegerField(null = True)
    is_staff     = models.BooleanField(default = False)
    is_active    = models.BooleanField(default = True)
    kakao_code   = models.IntegerField(null = True)
    room         = models.ManyToManyField("rooms.Room", through="Like", related_name="user_likes")
    
    objects         = UserManager()
    USERNAME_FIELD  = "email"
    REQUIRED_FIELDS = ("name", "phone_number",)
    
    class Meta:
        db_table = 'users'
        swappable = 'AUTH_USER_MODEL'
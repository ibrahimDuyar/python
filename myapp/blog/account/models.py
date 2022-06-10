from re import X
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class CastomUserModel(AbstractUser):

    image = models.FileField(upload_to='user/', blank=True, null=True)
    admin = models.BooleanField(default=False)

    class Meta:
        
        db_table = 'User'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):

        return self.username
from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from datetime import date

# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50,blank=True,null=True,unique=True)
    email = models.EmailField(('email address'),unique=True)
    nativename = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=10)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']
    def __str__(self):
        return'{}'.format(self.email) 
        
    
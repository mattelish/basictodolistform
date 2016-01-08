from django.db import models
import datetime
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from address.models import AddressField

# Create your models here.

class Register(models.Model):
     First_name = models.CharField(max_length=200)
     Last_name = models.CharField(max_length=200)
     Sex = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
     Phone_number = PhoneNumberField()
     Email = models.EmailField(max_length=200)
     Address =AddressField()
     pub_date = models.DateTimeField('date')
    
     def was_published_recently(self):
         now = timezone.now()
         return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
     def __str__(self):              # __unicode__ on Python 2
        return self.First_name

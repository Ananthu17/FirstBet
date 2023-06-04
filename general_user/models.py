from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class BaseUser(AbstractUser):
    # Add your custom fields here
    country = models.CharField(max_length=100)
    phone_number = PhoneNumberField(unique=True)
    tc_status = models.BooleanField(default=False)

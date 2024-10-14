from django.db import models;
from django.contrib.auth.models import AbstractUser;

# Create your models here.
class Investment_Profiles(models.Model):
    profile = models.CharField(max_length=12);

class Users(AbstractUser):
    first_name = models.CharField(max_length=20);
    last_name = models.CharField(max_length=20);
    email = models.EmailField(unique=True);
    password = models.CharField(max_length=40);
    investment_profile = models.ForeignKey(Investment_Profiles, on_delete=models.CASCADE);

    USERNAME_FIELD = 'email';
    REQUIRED_FIELDS = [];
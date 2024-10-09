from django.db import models

# Create your models here.
class Investment_Profiles(models.Model):
    profile = models.CharField(max_length=12);

class Users(models.Model):
    first_name = models.CharField(max_length=20);
    last_name = models.CharField(max_length=20);
    email = models.EmailField();
    password = models.CharField(max_length=40);
    investment_profile = models.ForeignKey(Investment_Profiles, on_delete=models.CASCADE);
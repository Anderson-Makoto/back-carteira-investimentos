from django.db import models
from users.models import Users;
import datetime;

# Create your models here.
class Asset_Types(models.Model):
    asset_type = models.CharField(max_length=10);

class Assets(models.Model):
    asset_type = models.ForeignKey(Asset_Types, on_delete=models.CASCADE);
    asset_name = models.CharField(max_length=20);

class User_Investments(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE);
    capital = models.DecimalField(max_digits=8, decimal_places=2);
    assets = models.ForeignKey(Assets, on_delete=models.CASCADE);
    created_at = models.DateTimeField(auto_now_add=True);
    is_buying = models.BooleanField();
    amount = models.IntegerField();
    
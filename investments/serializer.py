from rest_framework import serializers;
from .models import User_Investments, Assets;

class UserInvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Investments;
        fields = '__all__';
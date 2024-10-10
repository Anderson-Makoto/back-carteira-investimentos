from django.urls import path;
from .views import save_user_investment;

urlpatterns = [
    path('save_investment/', save_user_investment, name='save_user_investment'),
];
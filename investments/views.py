from django.shortcuts import render
from rest_framework.decorators import api_view;
from rest_framework.response import Response;
from rest_framework import status;
from .serializer import UserInvestmentSerializer;
from .services.investments_service import InvestmentsService;

investments_service = InvestmentsService();

@api_view(['POST'])
def save_user_investment(request):
    global investments_service;
    investments_service.create_investment(request.data);
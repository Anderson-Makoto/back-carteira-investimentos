from django.shortcuts import render
from rest_framework.decorators import api_view;
from rest_framework import status;
from .serializer import UserInvestmentSerializer;
from rest_framework.response import Response;
from django.forms.models import model_to_dict;
from .services.investments_service import InvestmentsService;
from helpers import http_response_error_handler;

investments_service = InvestmentsService();

@api_view(['POST'])
def save_user_investment(request):
    global investments_service;
    try:
        user_investment = investments_service.create_investment(request.data);

        return Response(status=status.HTTP_201_CREATED, data=model_to_dict(user_investment));
    except Exception as e:
        return http_response_error_handler(e);
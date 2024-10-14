from rest_framework.decorators import api_view;
from rest_framework import status;
from rest_framework.response import Response;
from django.forms.models import model_to_dict;
from .services.user_service import UserService;
from helpers import http_response_error_handler;

user_service = UserService();

@api_view(['POST'])
def save_user(request):
    global user_service;
    try:
        user_model = user_service.create_user(request.data);

        return Response(status=status.HTTP_201_CREATED, data=model_to_dict(user_model));
    except Exception as e:
        return http_response_error_handler(e);
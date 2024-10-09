from rest_framework.response import Response;
from rest_framework import status;

INVESTMENT_PROFILES = {
    1: 'moderado',
    2: 'arrojado',
    3: 'conservador',
};

ASSET_TYPES = {
    1: 'variavel',
    2: 'fixo',
};

class BadRequestException(Exception):
    pass;

class UnauthorizedException(Exception):
    pass;

class ServerErrorException(Exception):
    pass;

class NotFoundErrorException(Exception):
    pass;

def http_response_error_handler(exception: Exception) -> Response:
    if isinstance(exception, BadRequestException):
        return Response(status=status.HTTP_400_BAD_REQUEST, data=str(exception));
    elif isinstance(exception, UnauthorizedException):
        return Response(status=status.HTTP_401_UNAUTHORIZED, data=str(exception));
    elif isinstance(exception, NotFoundErrorException):
        return Response(status=status.HTTP_404_NOT_FOUND, data=str(exception));
    else:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data=str(exception));
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers


def custom_exception_handler(exc, context):
    # Check if the exception is a validation error
    if isinstance(exc, serializers.ValidationError):
        errors = exc.detail
        # Customize the error response as needed
        response_data = {
            'status_code': status.HTTP_400_BAD_REQUEST,
            'errors': errors,
        }
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
    
    return exception_handler(exc, context)
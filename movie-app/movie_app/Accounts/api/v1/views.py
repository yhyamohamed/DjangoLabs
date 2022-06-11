from django.core.exceptions import ObjectDoesNotExist
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import status, routers, serializers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import logout
from .serializers import UserSerializer


@api_view(['POST'])
@permission_classes([])
def signup(request):
    serializer = UserSerializer(request.data)
    response = {'data': None, 'status': status.HTTP_201_CREATED}
    if serializer.is_valid():
        serializer.save()
        response['data'] = serializer.data
    else:
        response['data'] = serializer.errors
        response['status'] = status.HTTP_400_BAD_REQUEST
    return Response(**response)


@api_view(['POST'])
def logout(self, request):
    try:
        request.user.auth_token.delete()
    except (AttributeError, ObjectDoesNotExist):
        pass

    logout(request)
    return Response({"success": "Successfully logged out."}, status=status.HTTP_200_OK)

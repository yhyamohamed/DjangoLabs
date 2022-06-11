from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import status, routers, serializers, viewsets
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ActorSerializer
from ...models import Actor


@api_view(['GET'])
def index(request):
    all_movies = Actor.objects.all()
    serializer = ActorSerializer(all_movies, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


class ShowActor(RetrieveAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

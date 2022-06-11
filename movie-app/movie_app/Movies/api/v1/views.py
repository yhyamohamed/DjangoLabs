from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import status, routers, serializers, viewsets
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .serializers import MovieSerializer, MovieCreateSerializer
from ...models import Movie


@api_view(['GET'])
def index(request):
    all_movies = Movie.objects.all()
    serializer = MovieSerializer(all_movies, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_movie(request):
    response = {'data': None, 'status': status.HTTP_201_CREATED}
    serializer = MovieSerializer(date=request.data)

    if serializer.is_valid():
        serializer.save()
        response['data'] = serializer.data
    else:
        response['data'] = serializer.errors
        response['status'] = status.HTTP_400_BAD_REQUEST
    return Response(**response)


@api_view(['PUT', 'PATCH'])
def update_movie(request, id):
    movie = Movie.objects.filter(pk=id).first()
    serializer = MovieSerializer(instance=movie, data=request.data)
    if request.method == 'PATCH':
        serializer = MovieSerializer(instance=movie, data=request.data, partial=True)
    response = {'data': None, 'status': status.HTTP_201_CREATED}
    if serializer.is_valid():
        serializer.save()
        response['data'] = serializer.data
    else:
        response['data'] = serializer.errors
        response['status'] = status.HTTP_400_BAD_REQUEST
    return Response(**response)


@api_view(['DELETE'])
def delete_movie(request, id):
    Movie.objects.get(pk=id).delete()
    return Response(data={'response', 'Entry deleted'}, status=status.HTTP_204_NO_CONTENT)


class AllMovies(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class ShowMovie(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class CreateMovie(CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieCreateSerializer


class EditMovie(UpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class DeleteMovie(DestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

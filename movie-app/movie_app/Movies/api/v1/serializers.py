from rest_framework import serializers

from Movies.models import Movie
from Actors.api.v1.serializers import ActorSerializer


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Movie
        depth = 1


class MovieCreateSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)

    class Meta:
        fields = '__all__'
        model = Movie
        depth = 1

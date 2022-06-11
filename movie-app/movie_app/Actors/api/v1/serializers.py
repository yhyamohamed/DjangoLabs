from rest_framework import serializers

from Actors.models import Actor


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Actor
        depth = 1

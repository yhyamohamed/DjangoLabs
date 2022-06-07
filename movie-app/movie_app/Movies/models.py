from datetime import datetime

from django.db import models


class Movie(models.Model):
    name = models.fields.CharField(max_length=150)
    production_year = models.fields.DateTimeField(default=datetime.now)
    creation_time = models.fields.DateTimeField(auto_now_add=True)
    update_time = models.fields.DateTimeField(auto_now=True)
    actors = models.ManyToManyField('Actors.Actor')
    director = models.fields.CharField(max_length=100, verbose_name='Director', default='unknown')

    def __str__(self):
        return self.name

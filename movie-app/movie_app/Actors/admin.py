from django.contrib import admin
from django.utils.html import format_html

from .models import Actor


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'image', 'movies', 'age']
    search_fields = ['name']
    list_filter = ['gender']
    fieldsets = (
        ('About', {'fields': ['image', 'name', 'gender', 'age']}),
        ('Movies', {'fields': ['movies']})
    )

    def movies(self, obj):
        movies = [movie.name for movie in obj.movie_set.all()]
        return len(movies)

    def age(self, obj):
        return len(obj.name) + 30

    def image(self, obj):
        return format_html('<img src="{}" style="height:100px;width:100px"/>'.format(obj.profile_picture.url))

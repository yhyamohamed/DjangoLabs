from django.contrib import admin
from .models import Director, Movie


class MovieInline(admin.TabularInline):
    model = Movie
    extra = 1


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['name', 'movies_custom', 'movie']
    search_fields = ['movie__name', 'name']

    # readonly_fields = ['movies']

    inlines = [MovieInline]

    def movies_custom(self, obj):
        return obj.movie


admin.site.register(Movie)

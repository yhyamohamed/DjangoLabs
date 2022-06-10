from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse

from .forms import MovieForm
from .models import Movie


def index(request):
    movies = Movie.objects.all()
    print(movies)
    return render(request, 'Movies/Movies_list.html', {'movies': movies})

@login_required
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save()
            return redirect(reverse('Movies:all-Movies'))
    else:
        form = MovieForm()
    return render(request, 'Movies/create_movie.html', {'form': form})


def show(request, **kwargs):
    pass


def delete_movie(request, **kwargs):
    movie_id = kwargs.get('id')
    Movie.objects.filter(id=movie_id).delete()
    messages.warning(request, f'Well movie NO. {movie_id} is deleted')
    return redirect(reverse('Movies:all-Movies'))


def edit(request, id):
    movie = Movie.objects.get(pk=id);

    if request.method == 'GET':
        form = MovieForm(instance=movie)
        return render(request, 'Movies/edit_movie.html', {'form': form, 'movie': movie})
    else:
        form = MovieForm(request.POST,instance=movie)
        if form.is_valid():
            movie = form.save()
            return redirect(reverse('Movies:all-Movies'))

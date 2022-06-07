from django.contrib import messages
from django.shortcuts import render, redirect, reverse

from .forms import ActorForm
from .models import Actor


def index(request):
    actors = Actor.objects.all()
    return render(request, 'Actors/Actors_list.html', {'actors': actors})


def add_actor(request):
    if request.method == 'POST':
        form = ActorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('Actors:all-Actors'))
    else:
        form = ActorForm()
    return render(request, 'Actors/create_actor.html', {'form': form})


def show(request, **kwargs):
    pass


def delete_actor(request, **kwargs):
    actor_id = kwargs.get('id')
    Actor.objects.filter(id=actor_id).delete()
    messages.warning(request, f'Well actor NO. {actor_id} is deleted')
    return redirect(reverse('Actors:all-Actors'))


def edit(request, id):
    actor = Actor.objects.get(pk=id);

    if request.method == 'GET':
        form = ActorForm(instance=actor)
        return render(request, 'Actors/edit_actor.html', {'form': form, 'actor': actor})
    else:
        form = ActorForm(request.POST, request.FILES, instance=actor)
        if form.is_valid():
            actor = form.save()
            messages.success(request, f'Well actor NO. {actor.id} is updated')
            return redirect(reverse('Actors:all-Actors'))

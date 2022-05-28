from copy import deepcopy

from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

tasks = [
    {'name': 'do some thing', 'description': 'eat champions breakfast', 'is_done': False, 'priority': 1},
    {'name': 'walk the dog', 'description': 'walk zeus along the sea ', 'is_done': False, 'priority': 2},
    {'name': 'finish work', 'description': 'finish work tasks', 'is_done': False, 'priority': 4},
    {'name': 'do another thing', 'description': 'add any desc here', 'is_done': False, 'priority': 5}

]

backup_list = deepcopy(tasks)


def index(request):
    return render(request, 'todo/index.html', context={'tasks': tasks})


def show(request, **kwargs):
    task_id = kwargs.get('id')
    founded_task = tasks[task_id - 1]
    return render(request, 'todo/taskDetails.html', context={'task': founded_task})


def mark_task_as_done(request, **kwargs):
    task_id = kwargs.get('id')
    founded_task = tasks[task_id - 1]
    founded_task['is_done'] = True
    messages.success(request, f'Well done dude ! task : {founded_task["name"]} is done')
    return redirect(reverse('todo:all-tasks'))


def mark_task_as_not_done(request, **kwargs):
    task_id = kwargs.get('id')
    founded_task = tasks[task_id - 1]
    founded_task['is_done'] = False
    messages.warning(request, f'Well sh** happens ! task : {founded_task["name"]} is not done')
    return redirect(reverse('todo:all-tasks'))


def delete_task(request, **kwargs):
    task_id = kwargs.get('id')
    founded_task = tasks[task_id - 1]
    tasks.pop(task_id - 1)
    messages.info(request, f' task : {founded_task["name"]} is deleted')
    return redirect(reverse('todo:all-tasks'))


def refresh_list(request):
    global tasks
    tasks = deepcopy(backup_list)
    messages.success(request, f'list refreshed ')
    return redirect(reverse('todo:all-tasks'))


def api_call(request):
    return render(request, 'todo/apiCall.html')

from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.index, name='all-tasks'),
    path('<int:id>', views.show, name='task-details'),
    path('done/<int:id>', views.mark_task_as_done, name='task-done'),
    path('not-done/<int:id>', views.mark_task_as_not_done, name='task-not-done'),
    path('delete/<int:id>', views.delete_task, name='delete-task'),
    path('refresh-list', views.refresh_list, name='refresh-tasks-list'),
    path('weather-Api', views.api_call, name='weather-api'),



]

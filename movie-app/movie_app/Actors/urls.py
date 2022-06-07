from django.urls import path
from . import views

app_name = 'Actors'
urlpatterns = [
    path('', views.index, name='all-Actors'),
    path('create', views.add_actor, name='create'),
    path('<int:id>', views.show, name='show'),
    path('delete/<int:id>', views.delete_actor, name='delete-actor'),
    path('Edit/<int:id>', views.edit, name='edit-actor'),
]

from django.urls import path
from . import views

app_name = 'Movies'
urlpatterns = [
    path('', views.index, name='all-Movies'),
    path('create', views.add_movie, name='create'),
    path('<int:id>', views.show, name='show'),
    path('delete/<int:id>', views.delete_movie, name='delete-movie'),
    path('Edit/<int:id>', views.edit, name='edit-movie'),
]

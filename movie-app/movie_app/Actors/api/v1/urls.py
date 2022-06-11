from django.urls import path
from . import views

app_name = 'Actors-api-v1'
urlpatterns = [
    path('', views.index, name='all-Actors'),
    path('<int:pk>', views.ShowActor.as_view(), name='show'),
    # path('create', views.add_movie, name='create'),
    # path('<int:id>', views.show, name='show'),
    # path('delete/<int:id>', views.delete_movie, name='delete-movie'),
    # path('Edit/<int:id>', views.edit, name='edit-movie'),
]

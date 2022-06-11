from django.urls import path
from . import views

app_name = 'Movies-api-v1'

urlpatterns = [
    # generics views
    # path('', views.AllMovies.as_view(), name='all-Movies'),
    # path('<int:pk>', views.ShowMovie.as_view(), name='show'),
    # path('create', views.CreateMovie.as_view(), name='create'),
    # path('<int:pk>/edit', views.EditMovie.as_view(), name='edit'),
    # path('<int:pk>/delete', views.DeleteMovie.as_view(), name='delete'),
    # function bassed views
    path('', views.index, name='all-Movies'),
    path('create', views.create_movie, name='create'),
    path('<int:id>/edit', views.update_movie, name='edit'),
    path('<int:id>/delete', views.update_movie, name='delete'),

]

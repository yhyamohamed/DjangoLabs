from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'Accounts-api-v1'
urlpatterns = [
    path('login', obtain_auth_token),
    path('signup', views.signup, name='signup'),
]

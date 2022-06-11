from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    date_of_birth = models.fields.DateTimeField(verbose_name='BD',null=True,blank=True)
    profile_picture = models.ImageField(default='default.png', upload_to='users')

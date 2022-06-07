from django.db import models


class Actor(models.Model):
    GENDER = (('M', 'M'), ('F', 'F'))
    name = models.fields.CharField(max_length=60)
    gender = models.fields.CharField(choices=GENDER, max_length=1, default='M')
    profile_picture = models.ImageField(default='default.png', upload_to='actors')

    def __str__(self):
        return self.name

from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def my_handler(sender, **kwargs):
    print(sender)
    # send_mail(
    #     'Hola from our App Movie' ,#subject
    #     sender.username+' has been created ',#message
    #     'our@mail.com',#from
    #     'user.email',#to
    # )

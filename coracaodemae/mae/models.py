from django.db import models
from django.dispatch.dispatcher import receiver
from django_facebook.models import FacebookModel, FacebookProfileModel
from django.db.models.signals import post_save
from django_facebook.utils import get_user_model, get_profile_model
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


class Mae(FacebookProfileModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    teste = models.IntegerField()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Mae.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

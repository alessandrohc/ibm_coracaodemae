from django.db import models
from django.dispatch.dispatcher import receiver
from django_facebook.models import FacebookModel
from django.db.models.signals import post_save
from django_facebook.utils import get_user_model, get_profile_model
from django.conf import settings

# Create your models here.


class Mae(FacebookModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    @receiver(post_save)
    def create_profile(sender, instance, created, **kwargs):
        """Create a matching profile whenever a user object is created."""
        if sender == get_user_model():
            user = instance
            profile_model = get_profile_model()
        if profile_model == Mae and created:
            profile, new = Mae.objects.get_or_create(user=instance)

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from library.models import Library


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_library(sender, instance, created, **kwargs):
    if created:
        Library.objects.create(user=instance)
        token = Token.objects.create(user=instance)
        print(token.key)

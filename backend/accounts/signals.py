from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Creator, User, Viewer


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_viewer:
            Viewer.objects.create(user=instance)
        if instance.is_creator:
            Creator.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.is_viewer:
        instance.viewer.save()
    if instance.is_creator:
        instance.creator.save()

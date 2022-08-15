from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Video


@receiver(m2m_changed, sender=Video.users_favorites.through)
def users_favorite_changed(sender, instance, **kwargs):
	# Call the function if the signal has been launched by the sender
	instance.favorites = instance.users_favorites.count()
	instance.save()

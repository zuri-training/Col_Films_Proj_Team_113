from hashlib import blake2b
from random import random
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from .managers import UserManager


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(unique=True)
    email_verified = models.BooleanField(default=False)

    is_viewer = models.BooleanField(default=False)
    is_creator = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        ordering = ['email']
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        """String representation for the User model"""
        return self.email


class Viewer(models.Model):
    """ Model for storing a viewer instance. """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name='viewer')
    about = models.TextField(blank=True)
    image = models.ImageField(upload_to='viewer/images', blank=True)

    def __str__(self):
        return f"{self.user.username} profile"


class Creator(models.Model):
    """Model for storing a creator instance"""
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        related_name='creator')
    about = models.TextField(blank=True)
    image = models.ImageField(upload_to='creator/images', blank=True)

    def __str__(self):
        return f"{self.user.username} profile"

from re import I
from django.urls import reverse
from random import random
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.core.exceptions import ValidationError

from .managers import UserManager


def validate_school_email(email):
    """Verifies that the email has a .edu extension."""
    if ".edu" not in email.split("@")[1]:
        raise ValidationError("Your email has to be a school email.")
    else:
        return email


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('email'),
                              unique=True,
                              validators=[validate_school_email])
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
    school = models.CharField(
        _("School"), max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} profile"

    def get_absolute_url(self):
        return reverse("accounts:profile", kwargs={"pk": self.pk})

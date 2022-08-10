from hashlib import blake2b
from random import random
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

from .managers import UserManager
from .utils import generate_random_id


class User(AbstractUser):
    """User model."""

#     email = models.EmailField(_('email address'),
#                               unique=True)
#     username = models.CharField(max_length=150, unique=True)
#     first_name = models.CharField(max_length=150, blank=True)
#     is_active = models.BooleanField(default=False)

# class CustomAccountManager(BaseUserManager):
#     # username = models.TextField(unique=True)
#     # email = models.EmailField(unique=True)

#     def create_superuser(self, email, username, password, **other_fields):

#         other_fields.setdefault('is_staff', True)
#         other_fields.setdefault('is_superuser', True)
#         other_fields.setdefault('is_active', True)

#         if other_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must be assigned to is_staff=True')
    
    
        
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    slug = models.SlugField(blank=True, unique=True)

    is_viewer = models.BooleanField(default=False)
    is_creator = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        ordering = ['email']
        verbose_name = 'User'

    def __str__(self):
        """String representation for the User model"""
        return self.email


class Viewer(models.Model):
    """ Model for storing a viewer instance. """
    user = models.OneToOneField(
        User,
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
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name='creator')
    about = models.TextField()
    image = models.ImageField(upload_to='creator/images')

    def __str__(self):
        return f"{self.user.username} profile"

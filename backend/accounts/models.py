from random import random
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

from .managers import CustomUserManager
from .utils import generate_random_id


# class UserBase(AbstractBaseUser, PermissionsMixin):

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
    username = models.TextField(unique=True)
    email = models.EmailField(unique=True)
    slug = models.SlugField(blank=True, unique=True)

    is_viewer = models.BooleanField(default=False)
    is_creator = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        ordering = ['email']
        verbose_name = 'User'

    def __str__(self):
        """String representation for the User model"""
        return self.email

    def generate_random_slug(self):
        random_slug = slugify(self.first_name + self.last_name + generate_random_id())
            
        while CustomUser.objects.filter(slug=random_slug).exists():
            random_slug = slugify(self.first_name + self.last_name + generate_random_id())
        return random_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_random_slug()

        super().save(*args, **kwargs)


class Viewer(models.Model):
    """ Model for storing a viewer instance. """
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        null=True,
        related_name='viewer')
    company_name = models.CharField(max_length=50)
    address = models.CharField(max_length=600)
    about = models.TextField()
    state = models.CharField(max_length=10)
    image = models.ImageField(upload_to='viewer/images')
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} profile"


class Creator(models.Model):
    """Model for storing a creator instance"""
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        null=True,
        related_name='creator')

    def __str__(self):
        return f"{self.user.username} profile"

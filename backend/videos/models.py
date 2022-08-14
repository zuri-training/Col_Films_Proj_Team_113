import uuid

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext as _

# from PIL import Image


class Category(models.Model):
    """Model representing a video category."""

    name = models.CharField(verbose_name=_('name'),
                            max_length=150,
                            db_index=True,
                            help_text=_('category name.'),
                            unique=True)
    slug = models.SlugField(verbose_name=_('slug'),
                            max_length=100,
                            unique=True)
    description = models.CharField(verbose_name=_('description'),
                                   max_length=100)
    image = models.ImageField(verbose_name=_('image'), upload_to='categories')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        """String for representing the category object."""
        return self.name

    def get_absolute_url(self):
        """Return the URL to access a particular instance of category."""
        return reverse('core:category_detail', kwargs={'slug': self.slug})


class Video(models.Model):
    """Video model"""

    PRIVATE = 'PR'
    PUBLIC = 'PU'
    PRIVACY_CHOICES = [
        (PRIVATE, 'Private'),
        (PUBLIC, 'Public'),
    ]

    GENERAL = 'G'
    PARENTAL = 'PG'
    MATURED = 'M'
    RATING_CHOICES = [
        (GENERAL, 'General Audience'),
        (PARENTAL, 'Parental Guidance Suggested'),
        (MATURED, 'Mature Audience Only'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name=_('videos'),
                             verbose_name=_('user'))
    title = models.CharField(verbose_name=_('title'),
                             max_length=250,
                             db_index=True,
                             help_text=_('Title of the video.'))
    # use uuid?
    slug = models.SlugField(verbose_name=_('slug'),
                            max_length=100,
                            unique=True)
    video_file = models.FileField(verbose_name=_('Video file'),
                                  upload_to='videos',
                                  validators=[FileExtensionValidator(['mp4'])],
                                  help_text=_('Path to the uploaded video.'))
    thumbnail = models.ImageField(verbose_name=_('thumbnail'),
                                  upload_to='thumbnails',
                                  validators=[FileExtensionValidator(
                                    ["jpg", "jpeg", "png", "webp"])],
                                  help_text=_('An image that will be used as a thumbnail.'))
    description = models.TextField(verbose_name=_('description'),
                                   max_length=1000,
                                   help_text=_('Description of the video.'))
    privacy = models.CharField(verbose_name=_('privacy'),
                               max_length=2,
                               choices=PRIVACY_CHOICES,
                               default=PUBLIC)
    movie_rating = models.CharField(verbose_name=_('movie rating'),
                                    max_length=2,
                                    choices=RATING_CHOICES)
    impressions = models.PositiveBigIntegerField(verbose_name=_('impressions'),
                                                 default=0,
                                                 help_text=_('View count for a video.'))
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name=_('videos'),
                                 verbose_name=_('categories'),
                                 blank=True)
    released = models.DateField(blank=True, null=True)
    enable_comments = models.BooleanField(verbose_name=_('enable comments'),
                                          default=True,
                                          help_text=_('Flag to turn on/off commenting'))
    created = models.DateTimeField(verbose_name=_('created'),
                                   auto_now_add=True,
                                   help_text=_('The date/time when the user uploaded the video'))
    updated = models.DateTimeField(verbose_name=_('updated'),
                                   auto_now=True,
                                   help_text=_('The date/time when the user made changes to the video information'))
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                       related_name=_('likes'),
                                       verbose_name=_('user likes'),
                                       blank=True,
                                       help_text=_('Users who added video to their likes.'))
    like_count = models.BigIntegerField(default=0)
    video_length = models.CharField(verbose_name=_('video length'),
                                    max_length=10,
                                    help_text=_('Length of the video in minutes:seconds'),
                                    blank=True)
    
    flag = models.BooleanField(verbose_name=_('_is flagged?'),
                               default=False,
                               help_text=_('If this video has been flagged for violations'))

    class Meta:
        ordering = ['-created']
        verbose_name = _('video')
        verbose_name_plural = _('videos')

    def get_absolute_url(self):
        return reverse('videos:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    # Untested code
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     thumb = Image.open(self.thumbnail.path)

    #     if thumb.height > 300 or thumb.width > 300:
    #         output_size = (300, 300)
    #         thumb.thumbnail(output_size)
    #         thumb.save(self.thumbnail.path)

class Comment(models.Model):
    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
        related_name='comments')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_comments')
    body = models.TextField(_('body'))
    created = models.DateTimeField(
        auto_now_add=True)
    active = models.BooleanField(
        default=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.user.username} - {self.video.title}'

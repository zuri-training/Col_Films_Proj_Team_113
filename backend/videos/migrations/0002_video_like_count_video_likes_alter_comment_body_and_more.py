# Generated by Django 4.1 on 2022-08-13 14:20

from django.conf import settings
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='like_count',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='video',
            name='likes',
            field=models.ManyToManyField(blank=True, default=None, related_name='like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(verbose_name='body'),
        ),
        migrations.AlterField(
            model_name='video',
            name='thumbnail',
            field=models.ImageField(help_text='An image that will be used as a thumbnail.', upload_to='thumbnails', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png', 'webp'])], verbose_name='thumbnail'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(help_text='Path to the uploaded video.', upload_to='videos', validators=[django.core.validators.FileExtensionValidator(['mp4'])], verbose_name='Video file'),
        ),
    ]

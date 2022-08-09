from django.db import models
from django.contrib.auth.models import User

from Col_Films_Proj_Team_113.backend import videos

# Create your models here.


# The watch later function will operate on the  video model 
# class Video(models.Model):
#     content_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=200)
#     creator = models.CharField(max_length=200)
#     video = models.FileField(upload_to='videos')



class WatchLater(models.Model):
    watch_id = models.AutoField(primary_key=True)
    # username = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_id = models.CharField(max_length=20000)
    
    def __str__(self):
        return self.username
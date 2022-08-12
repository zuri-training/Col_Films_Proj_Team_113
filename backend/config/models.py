# from django.db import models
# from django.contrib.auth.models import User


# class WatchLater(models.Model):
#     watch_id = models.AutoField(primary_key=True)
#     # username = models.CharField(max_length=100)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     video_id = models.CharField(max_length=20000)
    
#     def __str__(self):
#         return self.username
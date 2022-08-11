from django.contrib import admin

from Col_Films_Proj_Team_113.backend.accounts.models import User
from .models import movie,profile,user,video

admin.site.register(movie)
admin.site.register(profile)
admin.site.register(video)
admin.site.register(User)
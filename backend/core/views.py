from django.shortcuts import render
from videos.models import Video

def home(request):

    if request.user.is_authenticated:
        videos = Video.objects.all()

        template = 'core/home.html'
        context = {'videos': videos}
        return render(request, template, context)
    else:
        template = 'core/landing.html'
        context = {}
        return render(request, template, context)

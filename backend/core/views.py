from django.shortcuts import render
from videos.models import Category, Video

def home(request):

    if request.user.is_authenticated:
        videos = Video.objects.all()

        template = 'core/home.html'
        context = {'videos': videos}
        return render(request, template, context)
    else:
        categories = Category.objects.all()
        template = 'core/landing.html'
        context = {'categories': categories}
        return render(request, template, context)


def tour(request):
    videos = Video.objects.all()

    template = 'core/tour.html'
    context = {'videos': videos}
    return render(request, template, context)

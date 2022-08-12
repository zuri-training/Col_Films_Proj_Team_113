from django.shortcuts import render


def home(request):

    if request.user.is_authenticated:
        template = 'core/home.html'
        context = {}
        return render(request, template, context)
    else:
        template = 'core/landing.html'
        context = {}
        return render(request, template, context)

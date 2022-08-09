from django.shortcuts import render


def home(request):

    template = 'core/home.html'
    context = {}

    return render(request, template, context)

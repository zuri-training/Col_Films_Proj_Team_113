from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

from .models import Faq

# Create your views here.
def index(request):
    return HttpResponse('Hello World')

def all_faq(request):
    context ={'faqs': Faq.objects.all(),}
    return render(request, 'faq.html', context)
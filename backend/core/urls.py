from django.urls import path

from .views import home, tour

app_name = 'core'

urlpatterns = [
    path('tour/', tour, name='tour'),
    path('', home, name='home'),
]

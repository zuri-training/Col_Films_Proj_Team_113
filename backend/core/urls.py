from django.urls import path

from .views import home, tour, explore

app_name = 'core'

urlpatterns = [
    path('tour/', tour, name='tour'),
    path('explore/', explore, name='explore'),
    path('', home, name='home'),
]

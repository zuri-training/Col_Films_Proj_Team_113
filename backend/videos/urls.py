from django.urls import path

from . import views

app_name = 'videos'

urlpatterns = [
    path('create/', views.video_create, name='create'),
    path('<slug:slug>/', views.video_detail, name='detail'),
]

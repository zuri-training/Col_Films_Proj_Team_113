from django.urls import path

from . import views

app_name = 'videos'

urlpatterns = [
    path('create/', views.video_create, name='create'),
    path('<int:id>/favorite/',
		views.video_favorite,
		name='favorite'),

	path('<int:id>/unfavorite/',
		views.video_unfavorite,
		name='unfavorite'),
    path('<slug:slug>/', views.video_detail, name='detail'),
]

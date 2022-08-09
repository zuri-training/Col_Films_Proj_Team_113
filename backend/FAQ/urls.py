from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('faq/', views.all_faq, name='all_faq'),
]

from django.contrib import admin
from django.urls import include, path
from user import views as user_view
from django.contrib.auth import views as auth



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    # path('login/', user_view.login, name = 'login'),
    # path('logout/', auth.LogoutView.as_view(template_name ='user/index.html'), name ='logout'),
    # path('register/', user_view.register, name ='register'),
]

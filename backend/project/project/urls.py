from django.contrib import admin
from django.urls import include, path
from user import views as user_view
from django.contrib.auth import views as auth



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('login/', user_view.login, name = 'login'),
    path('logout/', auth.LogoutView.as_view(template_name ='user/index.html'), name ='logout'),
    path('register/', user_view.register, name ='register'),
]

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('video.urls'))
    ]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

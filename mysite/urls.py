from django.contrib import admin
from django.urls import path, include

from . views import *

########### untuk media #############
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404, handler500

# memanggil fungsi home yang ada didalam file views
from . views import *


urlpatterns = [
    path('admin/', admin.site.urls), 
    #apps
    path('dashboard/', include('blog.urls')),
    #path('user/',include('user.urls')),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('home/', home, name='home'),
    path('login/',login, name = 'login'),
    path('resep/', resep, name='api_blog'),
    #path('resep/detail/<str:key>', resep_detail, name='resep_detail'),
     path('logout/',logout_view, name = 'logout'),
]

######## untuk media ##########
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

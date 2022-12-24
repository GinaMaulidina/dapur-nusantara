from django.urls import path, include

from . views import *

urlpatterns = [
    path('tambah-user/',tambah_user, name='tambah_user'),
    path('',dashboard, name='dashboard'),
    path('user/',user, name='tabel_user'), 
    #path('blog/lihat/<str:id>',lihat_user, name='lihat_user'), 

    #path('blog/edit/<str:id>',edit_user, name='edit_user'),
    #path('blog/delete/<str:id>',delete_user, name='delete_user'),
    
] 


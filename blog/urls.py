from django.urls import path, include

from . views import *

urlpatterns = [
    path('',dashboard, name='dashboard'),
    path('blog/',blog, name='tabel_blog'), 
    path('tambah-blog/',tambah_blog, name='tambah_blog'),
    path('blog/lihat/<str:id>',lihat_blog, name='lihat_blog'), 
    path('blog/edit/<str:id>',edit_blog, name='edit_blog'),
    path('blog/delete/<str:id>',delete_blog, name='delete_blog'),
    path('user/',user, name='tabel_user'), 
    #path('tambah-user/',tambah_user, name='tambah_user'),
    #path('blog/lihat/<str:id>',lihat_user, name='lihat_user'), 
    #path('blog/edit/<str:id>',edit_user, name='edit_user'),
    #path('blog/delete/<str:id>',delete_user, name='delete_user'),
    
]


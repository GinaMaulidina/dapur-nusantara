from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
def dashboard(request):
    template_name = "back/dashboard.html"
    context = {
        'title':'dashboard',
    }
    return render (request, template_name, context)

def blog(request):
    template_name = "back/tabel_blog.html"
    context = {
         'title' : 'Tabel Blog',
             
    }
    return render (request, template_name, context)



def user(request):
    return HttpResponse('ini page user')
    template_name = 'back/tabel_user.html'
    user = User.objects.all()
    print(template_name)
    context = {
        'title': 'Tabel User',
        'user': user
    }
    return render(request, template_name, context)

def tambah_user(request):
    template_name = 'back/tambah_user.html'
    context = {
        'title' : 'tambah user'
    }
    return render (request, template_name, context)
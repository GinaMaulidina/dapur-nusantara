from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login 
from blog.models import Blog, Resep
from django.contrib.auth import logout
from django.http import HttpResponse
import requests

def index(request):
	template_name = 'front/index.html'
	blog = Blog.objects.all()
	context = {
		'title' : 'HOME',
		'blog':blog,
		
	}
	return render(request, template_name, context)

def about(request):
	template_name = 'front/about.html'
	context = {
		'title' : 'HOME',
	}
	return render(request, template_name, context)

def home(request):
	template_name = 'front/home.html'
	context = {
		'title' : 'HOME',
	}
	return render(request, template_name, context)

def login(request):
	if request.user.is_authenticated:
		return redirect('home')
		
	template_name = 'account/login.html'
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		print(username, password)
		user = authenticate(request, username=username, password=password)
		if user is not None:
			#data ada
			print('username Anda Benar')
			auth_login(request, user)
			return redirect('home')
		else:
			#data tidak ada
			print('Usename Anda Salah')
	context = {
		'title' : 'login'
	}
	return render(request, template_name, context)

def resep(request):
	URL = "https://masak-apa-tomorisakura.vercel.app/api/recipes/"
	s = requests.get(url = URL)
	data = s.json()
	resep = data['results']
	template_name = 'front/resep.html'
	# resep = Resep.objects.all()
	context = {
        'title' : 'Resep',
        'resep' : resep,
    }
	return render(request, template_name, context)

def resep_detail(request, key):
    template_name = 'front/resep_detail.html'
    resep = Resep.objects.get(key=key) 
    dresep = Resep.objects.all()    
    context = {
        'title' : 'Resep',
        'resep' : resep,
        'dresep': dresep
    }
    return render(request, template_name, context)

def logout_view(request):
	logout(request)
	return redirect('home')

	
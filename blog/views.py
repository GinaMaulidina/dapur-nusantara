from django.shortcuts import render, redirect
from. models import Blog, Kategori, Resep
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.

def is_operator(user):
    if user.groups.filter(name='Operator').exists():
        return True
    else:
        return False

@login_required
@user_passes_test(is_operator)
def dashboard(request):
    template_name = "back/dashboard.html"
    context = {
        'title':'dashboard',
    }
    return render (request, template_name, context)

def blog(request):
    template_name = "back/tabel_blog.html"
    blog = Blog.objects.all()
    context = {
         'title' : 'Tabel Blog',
         'blog':blog,
        
    }
    return render (request, template_name, context)
@login_required
def tambah_blog(request):
    template_name = "back/tambah_blog.html"
    kategori = Kategori.objects.all()
    print(kategori)
    if request.method == "POST":
        nama = request.POST.get('nama')
        judul = request.POST.get('judul')
        deskripsi = request.POST.get('deskripsi')
        kategori = request.POST.get('kategori')
        #panggil katagory
        kat = Kategori.objects.get(nama=kategori)
        Blog.objects.create(
            nama = nama,
            judul = judul,
            deskripsi = deskripsi,
            kategori = kat,
        )
        return redirect(blog)
    context = {
        'title' : 'Tambah blog',
        'kategori':kategori,
    }
    return render (request, template_name, context)
@login_required
def lihat_blog(request, id):
    template_name = "back/lihat_blog.html"
    blog = Blog.objects.get(id=id)
    context = {
        'title' : 'Lihat blog',
        'blog':blog,
    }
    return render (request, template_name, context)
@login_required
def edit_blog(request, id):
    template_name = "back/edit_blog.html"
    a = Blog.objects.get(id=id)
    if request.method == "POST":
        judul = request.POST.get("judul")
        deskripsi = request.POST.get("deskripsi")
        #simpan data
        a.judul = judul
        a.deskripsi = deskripsi
        a.save()
        return redirect(blog)
    context = {
        'title' : 'Edit blog',
        'blog':a,
    }
    return render (request, template_name, context)
@login_required
def delete_blog(request, id):
    Blog.objects.get(id=id).delete()
    return redirect(blog)
    
def user(request):
    user = User.objects.all()
    template_name = "back/tabel_user.html"
    context = {
        'title' : 'Tabel User',
        'user' : user
    }
    return render (request, template_name, context)

#api
def api_blog(request):
    URL = "http://api-food-recipe.herokuapp.com/recipe"
    s = request.get(url = URL)
    data = s.json()
    resep = data['results']
    for a in data["results"]:
        print(a['key'])
        cek_resep = Resep.objects.filter(key=a['key'])
        if cek_resep.exists():
            resep = cek_resep.first()
            resep.title = a['title']
            resep.thumb = a['thumb']
            resep.key = a['key']
            resep.times = a['times']
            resep.save()
        else:
            Resep.objects.create(
				title = a['title'],
				thumb = a['thumb'],
				key = a['key'],
				times = a['times'],
			)
    ambil_resep = Resep.objects.all()
    
    for ambil in ambil_resep:
        url_detail_resep = "http://api-food-recipe.herokuapp.com/recipe{}".format(ambil.key)
        print(url_detail_resep)
        s = request.get(url_detail_resep,ambil.key)
        data = s.json()['results']
        ambil.step = data['step']
        ambil.ingredient = data['ingredient']
        ambil.save()
        return HttpResponse("<h1> Berhasil Masuk </h1>")


     
    

 
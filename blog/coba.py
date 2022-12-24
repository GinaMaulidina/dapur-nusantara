def tambah_user(request):
    template_name = "back/tambah_user.html"
        User.objects.create(
            nama = nama,
            email = email,
            alamat= alamat,
    context = {
        'title' : 'Tambah_user',
       
    return render (request, template_name, context)


def lihat_user(request, id):
    template_name = "back/lihat_blog.user"
    User = Blog.objects.get(id=id)
    context = {
        'title' : 'Lihat user',
        'user':user,
    }
    return render (request, template_name, context)

def edit_user(request, id):
    template_name = "back/edit_User.html"
    a = User.objects.get(id=id)
    if request.method == "POST":
        nama = request.POST.get("nama")
        email = request.POST.get("email")
        #simpan data
        a.nama = nama
        a.email = email
        a.save()
        return redirect(user)
    context = {
        'title' : 'Edit user',
        'user':a,
    }
    return render (request, template_name, context)


def delete_user(request, id):
    User.objects.get(id=id).delete()
    return redirect(user)
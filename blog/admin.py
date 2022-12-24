from django.contrib import admin
from.models import *
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('nama','judul','deskripsi','kategori','date')

admin.site.register(Kategori)

admin.site.register(Blog, BlogAdmin)

class ApiAdmin(admin.ModelAdmin):
    list_display = ['title', 'thumb', 'key', 'times', 'step', 'ingredient']
admin.site.register(Resep, ApiAdmin)

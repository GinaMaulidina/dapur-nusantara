from django.db import models

# Create your models here.

from django.contrib.auth.models import *
from django.db.models.fields.related import ForeignKey


class Kategori(models.Model):
    nama = models.CharField(max_length=20)

    def __str__(self):
        return self.nama
    class Meta:
        verbose_name_plural = "Kategori"



class Blog(models.Model):
    nama = models.CharField(max_length=100, blank=True, null=True)
    judul = models.CharField(max_length=100)
    deskripsi = models.TextField()
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "{}-{}".format(self.nama, self.judul)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Blog"


class Resep (models.Model):
    title = models.CharField(max_length=100)
    thumb = models.CharField(blank=True, null=True, max_length=50)
    key = models.CharField(max_length=100)
    times = models.CharField(max_length=50)
    step = models.TextField()
    ingredient = models.TextField()

    def __str__(self):
        return self.title

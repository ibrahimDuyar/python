from turtle import title
from django.db import models
from account.models import CastomUserModel
from ckeditor.fields import RichTextField
from django.utils.text import slugify
import random
# Create your models here.


class KategororiModel(models.Model):

    title = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='child')
    slug = models.SlugField(unique=True)


    def __str__(self):
        
        full_path = [self.title]

        k = self.parent

        while k is not None:
            full_path.append(k.title)

            k = k.parent
        
        return ' --> '.join(full_path[::-1])


    def save(self, *args, **kwargs):

        rr = random.randint(1000,3000)

        self.slug = slugify(self.title + '-' + str(rr))

        super().save(args, kwargs)


class UrunModel(models.Model):

    title = models.CharField(max_length=150)
    image = models.FileField(upload_to='urunler/', blank=True, null=True)
    slug  = models.SlugField(unique=True)
    aciklama = RichTextField()
    kategori = models.ForeignKey(KategororiModel, on_delete=models.CASCADE)
    yazar = models.ForeignKey(CastomUserModel, on_delete=models.CASCADE, blank=True, null=True)
    olusturma = models.DateTimeField(auto_now_add=True)
    degistirma = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):

        rr = random.randint(1000,3000)

        self.slug = slugify(self.title + '-' + str(rr))

        super().save(args, kwargs)


class YorumModel(models.Model):

    yazan_kisi = models.ForeignKey(CastomUserModel, on_delete=models.CASCADE, blank=True, null=True)
    yazilan_icerik = models.ForeignKey(UrunModel, on_delete=models.CASCADE, blank=True, null=True)
    yorum = models.TextField()



class ResimGaleriModel(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    urun = models.ForeignKey(UrunModel, on_delete=models.CASCADE, blank=True, null=True)
    image = models.FileField('urunler/', blank=True, null=True)


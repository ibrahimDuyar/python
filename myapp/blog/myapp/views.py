from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from myapp.models import *
from account.models import CastomUserModel

# Create your views here.

from myapp.form import YorumForm, YaziForm


def index(request):

    yazilar = UrunModel.objects.all()

    arama = request.GET.get('arama')

    if arama:

        yazilar = UrunModel.objects.filter(
            Q(title__icontains = arama) |
            Q(aciklama__icontains=arama)) 


    return render(request, 'index.html',{
        'yazilar':yazilar
    })



def yazar_panel(request, id):

    yazar = get_object_or_404(CastomUserModel, id=id)

    yazilar = UrunModel.objects.filter(yazar=yazar)


    return render(request, 'yazar.html', {
        'yazar':yazar,
        'yazilar':yazilar,
    })



def Kategori(request, slug):

    kategori = get_object_or_404(KategororiModel, slug=slug)

    yazilar = UrunModel.objects.filter(kategori=kategori)

    return render(request, 'kategori.html',{
        'kategori':kategori,
        'yazilar':yazilar,
    })



def yazilarim(request):

    yazilar = UrunModel.objects.filter(yazar=request.user)

    return render(request, 'yazilarim.html', {
        'yazilar':yazilar,
    })


def details(request, slug):

    yazi = get_object_or_404(UrunModel, slug=slug)
    images = ResimGaleriModel.objects.filter(urun=yazi)
    yorumlar = YorumModel.objects.filter(yazilan_icerik=yazi)


    #Yorum Form

    if request.method == "POST":

        form = YorumForm(request.POST)

        if form.is_valid():

            kullanici = form.save(commit=False)

            kullanici.yazan_kisi = request.user

            kullanici.yazilan_icerik = yazi

            kullanici.save()

            return redirect('details', slug=yazi.slug)


        else:
            return redirect('details', slug=yazi.slug)

    else:

        form = YorumForm()

    return render(request, 'details.html', {
        'yazi':yazi,
        'images':images,
        'yorumlar':yorumlar,
        'form':form,
    })



def yorum_duzenle(request, id):

    yorum = get_object_or_404(YorumModel, id=id)

    if yorum.yazan_kisi == request.user:

        if request.method == "POST":

            form = YorumForm(request.POST, instance=yorum)

            if form.is_valid():

                form.save()

                return redirect('details', slug=yorum.yazilan_icerik.slug)
        

        else:

            form = YorumForm(instance=yorum)
    

    
    
    




def yorum_sil(request, id):

    yorum = get_object_or_404(YorumModel, id=id)

    if yorum.yazan_kisi == request.user or yorum.yazilan_icerik.yazar == request.user:

        yorum.delete()

        return redirect('details', slug=yorum.yazilan_icerik.slug)
    

    return render(request, 'form1.html', {
        'yorum':yorum,
    })





def yazi_ekle(request):

    if request.method == 'POST':

        form = YaziForm(request.POST, request.FILES)

        if form.is_valid():

            kullanici = form.save(commit=False)

            kullanici.yazar = request.user

            kullanici.save()

            return redirect('yazilarim')
    

    else:
        form = YaziForm()

    
    return render(request, 'form1.html', {
        'form':form,
    })
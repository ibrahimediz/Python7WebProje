from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Gonderi
from .forms import PostForm

def gonderi_liste(request):
    Gonderiler =  Gonderi.objects.order_by('olus_zamani')
    return render(request, 'gonderi/gonderiliste.html', {"Gonderiler":Gonderiler})


def gonderi_detay(request,pk):
    gonderi = get_object_or_404(Gonderi,pk=pk)
    return render(request,'gonderi/gonderi_detay.html',{'Gonderi':gonderi})

def yeni_gonderi(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            gonderi = form.save(commit=False)
            kullanici = User.objects.get(username="edizadmin")
            # gonderi.yazar = request.user
            gonderi.yazar = kullanici
            gonderi.yayim_zaman = timezone.now()
            gonderi.save()
            return redirect('gonderi_detay', pk=gonderi.pk)
    else:
        form = PostForm()
    return render(request, 'gonderi/gonderiduzenle.html', {'form': form})

def gonderiduzenle(request, pk):
    gonderi = get_object_or_404(Gonderi, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=gonderi)
        if form.is_valid():
            gonderi = form.save(commit=False)
            kullanici = User.objects.get(username="edizadmin")
            # gonderi.yazar = request.user
            gonderi.yazar = kullanici
            gonderi.yayim_zaman = timezone.now()
            gonderi.save()
            return redirect('gonderi_liste')
    else:
        form = PostForm(instance=gonderi)
    return render(request, 'gonderi/gonderiduzenle.html', {'form': form})


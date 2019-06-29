from django.shortcuts import render
from .models import Service


def servislistele(request):
    servisler = Service.objects.filter(servis_aktif=False)
    return render(request,'Services/services.html',{"Servisler":servisler})

# Create your views here.

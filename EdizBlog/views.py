from django.shortcuts import render
from .models import Gonderi

def gonderi_liste(request):
    Gonderiler =  Gonderi.objects.order_by('olus_zamani')
    return render(request, 'gonderi/gonderiliste.html', {"Gonderiler":Gonderiler})
# Create your views here.

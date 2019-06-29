from django.shortcuts import render

def gonderi_liste(request):
    return render(request, 'gonderi/gonderiliste.html', {})
# Create your views here.

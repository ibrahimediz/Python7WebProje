from django.urls import path
from . import views

urlpatterns = [
    path('', views.gonderi_liste, name='gonderi_liste'),
    path('Gonderi/<int:pk>/', views.gonderi_detay, name='gonderi_detay'),
    path('Gonderi/yeni', views.yeni_gonderi, name='yeni_gonderi'),
    path('Gonderi/<int:pk>/duzenle/', views.gonderiduzenle, name='gonderiduzenle'),
]
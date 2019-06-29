from django.urls import path
from . import views

urlpatterns = [
    path('',views.servislistele,name="servislistele"),
]

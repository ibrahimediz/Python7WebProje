from django import forms

from .models import Gonderi

class PostForm(forms.ModelForm):

    class Meta:
        model = Gonderi
        fields = ('baslik', 'yazi',)
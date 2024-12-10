from django import forms
from .models import Cancion,Banda,Disco


class CancionForm(forms.ModelForm):
    class Meta:
        model = Cancion
        fields = ['title','author','year','description']

class DiscoForm(forms.ModelForm):
    class Meta:
        model = Disco
        fields = ['title','author','year','description']

class BandaForm(forms.ModelForm):
    class Meta:
        model = Banda
        fields = ['name','style','country','description']


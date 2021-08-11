from django import forms
from django.forms import fields, ModelForm
from .models import *

# class RegistroForm(forms.Form):
#     nombre = forms.CharField(label='Nombre', max_length=50)
#     apeido = forms.CharField(label='Apeido', max_length=50)
#     telefono  = forms.CharField(label='Telefono', max_length=50)
#     email = forms.CharField(label='Email', max_length=50)
    
class RegistroForm(ModelForm):
    class Meta:
        model = Registro
        fields= ['nombre', 'apeido', 'telefono', 'email']
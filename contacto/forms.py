from django import forms
from django.forms.widgets import Textarea

class FormularioContacto(forms.Form):
    nombre=forms.CharField(required=True)
    correo=forms.EmailField(label="Correo electrónico", required=True)
    contenido=forms.CharField(widget=Textarea)
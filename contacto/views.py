from django.forms.widgets import EmailInput
from .forms import *
from django.shortcuts import redirect, render
from django.core.mail import EmailMessage

# Create your views here.

def contacto(request):

    formularioContacto=FormularioContacto()

    if request.method=="POST":
        formularioContacto=FormularioContacto()

        nombre = request.POST.get("nombre")
        correo = request.POST.get("correo")
        contenido = request.POST.get("contenido")


        email=EmailMessage("<:: Mensaje automático de Django, enviado por {} con el correo {} ::>".format(nombre, correo),contenido,correo,["gachi1998@gmail.com"])

        email.send()

        return redirect("/Contacto/?valido")

    return render(request, "contacto/contacto.html", {"formularioContacto":formularioContacto})
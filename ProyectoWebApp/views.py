from django.shortcuts import render, HttpResponse

# Create your views here.
def inicio(request):
    return render(request, "ProyectoWebApp/home.html")




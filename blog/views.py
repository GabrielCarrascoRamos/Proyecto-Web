from django.shortcuts import render
from blog.models import *

# Create your views here.

def blog(request):
    categorías=Categoria.objects.all()
    posts=Post.objects.all()
    return render(request, "blog/blog.html", {"posts":posts, "categorías":categorías})

def categoria(request, categoriaID):    
    categoría=Categoria.objects.get(id=categoriaID)
    posts=Post.objects.filter(categoria=categoría)
    return render(request, "blog/categoria.html", {"categorías":categoría, "posts":posts})
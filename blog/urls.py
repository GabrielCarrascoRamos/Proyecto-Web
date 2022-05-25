from django.urls import path
from blog.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', blog),
    path("categoria/<int:categoriaID>/", categoria, name="categoria"),
]
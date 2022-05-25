from Servicios import views
from django.urls import path
from Servicios.views import *

urlpatterns = [
    path('', views.servicios, name="Servicios"),
]
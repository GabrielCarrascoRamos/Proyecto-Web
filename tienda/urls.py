from django.urls.conf import path
from .views import *

urlpatterns = [
    path("", tienda, name="tienda")

]

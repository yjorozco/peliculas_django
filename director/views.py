from django.shortcuts import render
from director.models import Pelicula, Director

# Create your views here.


def index(request):
    peliculas = Pelicula.objects.all()
    return render(request, "index.html",{"peliculas" : peliculas})
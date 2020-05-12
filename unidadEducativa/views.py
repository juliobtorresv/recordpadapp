from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Probando el funcionamiento de Unidad Educativa.")


def ingresoUE(request):
    return render(request, "ingresoUE.html")

def datosUE(request):
    mensaje="Datos recibidos: %r" %request.GET["nombreue"]
    return HttpResponse(mensaje)

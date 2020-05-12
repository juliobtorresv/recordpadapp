from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import authenticate

def index(request):
    if request.method == "POST":
        usuario=request.POST["usuario"]
        clave=request.POST["clave"]
        mensaje='Credenciales no Válidas'
        user = authenticate(username=usuario, password=clave)
        
        if user:
            request.session['usuario'] = True
            return render(request,"base.html",{"usuario":user})
        else:
            request.session['usuario'] = False
            return render(request,"index.html",{"error":mensaje})
    else:
        return render(request,"index.html")

def plantilla(request):
    return render(request,"plantilla.html")
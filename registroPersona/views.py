from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth import authenticate

# Create your views here.

def inicio(request):
    if request.method == "POST":
        usuario=request.POST["usuario"]
        clave=request.POST["clave"]
        user = authenticate(username=usuario, password=clave)
        if user:
            return render(request,"principal.html",{"email":usuario})
        else:
            return render(request,"index.html")
    else:
        return render(request,"index.html")
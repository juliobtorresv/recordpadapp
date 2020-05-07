from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

# Create your views here.

def inicio(request):
    if request.method == "POST":
        correo=request.POST["correo"]
        return render(request,"principal.html",{"email":correo})
    else:
        return render(request,"index.html")
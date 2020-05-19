from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import authenticate

def principal(request):
    return render(request,"baseApp.html")

def inicioSesion(request):
    return render(request,"registroPersona/index.html")

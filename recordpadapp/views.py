from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import authenticate

def principal(request):
    return render(request,"principal.html")
def servicios(request):
    return render(request,"servicios.html")


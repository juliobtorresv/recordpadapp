from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import authenticate
from registroPersona.forms import PersonaForm

# Create your views here.

def inicio(request):
    if request.method == "POST":
        usuario=request.POST["usuario"]
        clave=request.POST["clave"]
        mensaje='Credenciales no Válidas'
        user = authenticate(username=usuario, password=clave)
        
        if user:
            request.session['usuario'] = True
            return render(request,"principal.html",{"usuario":user})
        else:
            request.session['usuario'] = False
            return render(request,"index.html",{"error":mensaje})
    else:
        return render(request,"index.html")

def principal(request):
        
        if "usuario" in request.session:
            if request.session['usuario']:
                return render(request,"principal.html")
            else:
               # return render(request,"index.html")
                return HttpResponseRedirect("/")
        else:
            #return render(request,"index.html")
            return HttpResponseRedirect("/")

def persona_view(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request,"confirmacion.html")
        
    else:
        form = PersonaForm()
    return render(request, 'persona_form.html', {'form':form})

        

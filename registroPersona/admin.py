from django.contrib import admin
from registroPersona.models import Persona


# Register your models here.
class PersonaAdmin(admin.ModelAdmin):
    list_display=("cedula","nombre","apellido","email","telefono","representante")

admin.site.register(Persona, PersonaAdmin)

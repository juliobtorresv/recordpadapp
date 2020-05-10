from django import forms
from registroPersona.models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
                'cedula',
                'nombre',
                'apellido',
                'email',
                'telefono',
                'representante',
        ]
        labels = {
             'cedula':'CI',
                'nombre':'Nombre:',
                'apellido':'Apellido:',
                'email':'Correo Electrónico:',
                'telefono':'Teléfono:',
                'representante':'Es Representante S/N:',
        }
        widgets = {
                'cedula':forms.TextInput(attrs={'class':'form-control','placeholder':'Cédula de Identidad'}),
                'nombre':forms.TextInput(attrs={'class':'form-control'}),
                'apellido':forms.TextInput(attrs={'class':'form-control'}),
                'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Ingrese un correo'}),
                'telefono':forms.TextInput(attrs={'class':'form-control'}),
                'representante':forms.TextInput(attrs={'class':'form-control'}),
        }

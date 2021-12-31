from django import forms
from app.adopcion.models import Persona,Solicitud

class AdopcionForm(forms.ModelForm):
    class Meta:
        model=Persona

        fields= [ 
            'nombre',
            'apellido',
            'edad',
            'telefono',
            'email',
            'domicilio',
        ]
        labels={
            'nombre':'Nombre',
            'apellido':'Apellidos',
            'edad':'Edad ',
            'telefono':'Telefono',
            'email':'Email',
            'domicilio':'Domicilio',
        }
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'apellido':forms.TextInput(attrs={'class':'form-control'}),
            'edad':forms.TextInput(attrs={'class':'form-control'}),
            'telefono':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'domicilio':forms.TextInput(attrs={'class':'form-control'}),
        }


class solicitudForm(forms.ModelForm):
    class Meta:
        model=Solicitud
        fields=[
            'numero_mascotas',
            'razones',
        ]
        labels={
            'numero_mascotas':'Numero de mascotas',
            'razones':'Razones para adoptar',
        }
        widgets={
            'numero_mascotas':forms.TextInput(attrs={'class':'form-control'}),
            'razones':forms.Textarea(attrs={'class':'form-control'}),
        }

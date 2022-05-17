from django import forms

from app.adopcion.models import Persona
from app.mascota.models import Mascota, Vacuna


class MascotaForm(forms.ModelForm):
    class Meta:
        model=Mascota

        fields= [ 
            'nombre',
            'sexo',
            'edad_aproximada',
            'fecha_rescate',
            'persona',
            'vacuna',
            'imagen',
        ]
        labels={
            'nombre':'Nombre de la Mascota',
            'sexo':'Sexo',
            'edad_aproximada':'Edad aproximada',
            'fecha_rescate':'Fecha de rescate',
            'persona':'Adoptante',
            'vacuna':'Vacunas',
            'imagen':'Imagen de la mascota'
        }
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'sexo':forms.TextInput(attrs={'class':'form-control'}),
            'edad_aproximada':forms.TextInput(attrs={'class':'form-control'}),
            'fecha_rescate':forms.TextInput(attrs={'class':'form-control'}),
            'persona':forms.Select(attrs={'class':'form-control'}),
            'vacuna':forms.CheckboxSelectMultiple(),
        }


class MascotaApiForm(forms.Form):
    TIPO_SEXO = (
        ('Macho', 'Macho'),
        ('Hembra', 'Hembra'),
    )
    nombre = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    sexo = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), required=False, choices=TIPO_SEXO)
    edad_aproximada = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    fecha_rescate = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'date'}), required=False)
    persona = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), queryset=Persona.objects.all(), required=False)
    vacuna = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), required=False, queryset=Vacuna.objects.all())
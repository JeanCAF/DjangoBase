from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = (
            'fist_name',
            'last_name',
            'job',
            'departamento',
            'habilidades',
            'hoja_vida',
            'avatar',
        )
        widgets = {
            'habilidades': forms.CheckboxSelectMultiple()
        }
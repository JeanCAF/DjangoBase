from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import NewDepartamentoForm
from applications.persona.models import Empleado
from .models import Departamento

# Create your views here.

class NewDepartamentoview(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '.'

    def form_valid(self, form):

        depa = Departamento(
            name=form.cleaned_data['departamento'],
            shor_name=form.cleaned_data['shorname'],
        )
        depa.save()

        nombre = form.cleaned_data['nombre']
        apellidos = form.cleaned_data['apellidos']
        Empleado.objects.create(
            fist_name=nombre,
            last_name=apellidos,
            job='1',
            departamento=depa,
            hoja_vida='Nada'
        )
        return super(NewDepartamentoview, self).form_valid(form)
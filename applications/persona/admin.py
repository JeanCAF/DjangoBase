from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.

admin.site.register(Habilidades)


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'fist_name',
        'last_name',
        'departamento',
        'job',
        'full_name'
    )

    #metodo para agregar un dato que no esta en el modelo
    def full_name(self, obj):
        return obj.fist_name + ' ' + obj.last_name

    search_fields = ('fist_name', 'last_name')
    list_filter = ('job', 'departamento')

    filter_horizontal = ('habilidades',)

admin.site.register(Empleado, EmpleadoAdmin)

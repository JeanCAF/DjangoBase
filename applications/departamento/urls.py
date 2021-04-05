from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('new-departamento/', views.NewDepartamentoview.as_view(), name='nevo_departamento'),
]